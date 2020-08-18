

import numpy as np
import random

class Candidate:
    def __init__(self, puzzle):
        self.values = np.zeros((9, 9), dtype=np.int32)
        self.fitness = None
        self.originalPuzzle = puzzle
    
    def getBox(self, boxNum):
        """ Given box number from 0-8 return a list of the coordinates of the box """
        #Get coordinate of first row and column of box number
        firstRow = (boxNum // 3) * 3
        firstCol = (boxNum % 3) * 3

        #Get list of all coordinates of the current box
        boxCoords = [[firstRow+i, firstCol+j] for i in range(3) for j in range(3)]

        return boxCoords
    
    def initialise(self, puzzle):
        """ Intialise a candidate solution by filling in blank spaces in incomplete puzzle given"""

        populatedBoard = puzzle.copy()
        #For each box number 1-9...
        for boxNum in range(9):
        
            #Get box coordinates
            boxCoords = self.getBox(boxNum)
        
            #Get list of all coordinates in box that have a value that isnt 0
            valuesCoords = [i for i in boxCoords if populatedBoard[i[0]][i[1]] != 0]
            #Get list of all values in board for each coordinate in valuesCoords
            values = [populatedBoard[i[0]][i[1]] for i in valuesCoords]

            #Get list of the coordinates in boxCoords where value is 0
            zeroCoords = [i for i in boxCoords if populatedBoard[i[0]][i[1]] == 0]
            #Get list of all values that are not currently in the box and shuffle then
            toFillValues = [i for i in range(1,10) if i not in values]
            random.shuffle(toFillValues)
            fillCounter = 0
        
            #For each coordinate with a 0 in it...
            for x in zeroCoords:
           
                #fill board with numbers not currently in the board where there is currently a 0
                populatedBoard[x[0]][x[1]] = toFillValues[fillCounter]
                fillCounter += 1
        
        self.values = populatedBoard


    def updateFitness(self):
        """ Update candidate fitness (number of errors) """

        score = 0
        
        #For each row 1-9...
        for x in range(9):
            
            #Intialise sets
            rowSet = set()
            colSet = set()
            
            #For each value in row...
            for y in range(9):
                
                #Add numbers from each row into rowSet and numbers in columns into colSet
                rowSet.add(self.values[x][y])
                colSet.add(self.values[y][x])

            #Add to score the number of values in each row and column that is less than 9 (all the values)
            score += (9 - len(rowSet))
            score += (9 - len(colSet))       
        
        self.fitness = score


    def mutate(self, mutationRate):
        """ Picking a box, and then picking 2 values within the box to swap"""

        r = random.uniform(0, 1.1)

        if(r > mutationRate):

            while True:
                #Get random box number and get list of coordinates in that box
                boxNum = random.randrange(9)
                boxCoords = self.getBox(boxNum)
                print(boxNum)

                #Get list of cells in box that are not in original board and can be changed
                changeableCells = [i for i in boxCoords if self.originalPuzzle[i[0]][i[1]] == 0]

                if(len(changeableCells) >= 2):
                    break
        
            #Pick 2 random coordinates from the list of changeable cells
            a = random.sample(changeableCells, 1)
            b = random.sample(changeableCells, 1)
        
            #Swap values of 2 random coordinates
            self.values[a[0][0]][a[0][1]], self.values[b[0][0]][b[0][1]] = self.values[b[0][0]][b[0][1]] , self.values[a[0][0]][a[0][1]]





class Population:
    """ Population consists of a set of candidate solutions to the puzzle"""
    def __init__(self):
        self.candidates = []
    
    def intialise(self, populationSize, puzzle):
        """ Initialise all the candidate solutions in the population """
        
        for x in range(populationSize):
            newCandidate = Candidate(puzzle)
            newCandidate.initialise(puzzle)
            self.candidates.append(newCandidate)

        self.updateFitnesses()


    
    def updateFitnesses(self):
        """ Update all the fitnesses within the population """

        for candidate in self.candidates:
            candidate.updateFitness()


    def sort(self):
        """ Sort all the candidate solutions by their fitness from lowest to highest """
        self.candidates.sort(key=lambda x: x.fitness)





class Selection:

    def compete(self, candidates):
        """ Pick a random candidates from the population and get them to compete against each other"""

       #Picking 2 random individuals
        c1 = candidates[random.randint(0, len(candidates)-1)]
        c2 = candidates[random.randint(0, len(candidates)-1)]
        #Getting their fitness
        f1 = c1.fitness
        f2 = c2.fitness

        #Find the fittest and the weakest.
        if(f1 > f2):
            fittest = c1
            weakest = c2
        else:
            fittest = c2
            weakest = c1

        selection_rate = 0.85
        r = random.uniform(0, 1.1)
        while(r > 1):  
            #Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)
        if(r < selection_rate):
            #Lower than selection rate
            return fittest
        else:
            #Higher than selection rate
            return weakest



class Crossover:

    def crossover(self, parent1, parent2, crossoverRate):
        """ Takes 2 parents and a crossover rate and returns 2 new child Candidates created by swapping sections of the parents with each other"""

        child1 = Candidate(parent1.originalPuzzle)
        child2 = Candidate(parent2.originalPuzzle)
        
        # Make a copy of the parent genes.
        child1.values = np.copy(parent1.values)
        child2.values = np.copy(parent2.values)

        r = random.uniform(0, 1.1)
        while(r > 1):  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)
            
        # Perform crossover.
        if (r < crossoverRate):
            #Pick 2 crossover points, a box between 1-7 and a box between 1-8 to ensure the whole board isn't swapped 
            crossoverPoint1 = random.randint(0, 7)
            crossoverPoint2 = random.randint(1, 8)

            while(crossoverPoint1 == crossoverPoint2):
                crossoverPoint1 = random.randint(0, 8)
                crossoverPoint2 = random.randint(1, 9)

            #Make crossoverPoint1 to be the lesser of the 2 integers 
            if(crossoverPoint1 > crossoverPoint2):
                crossoverPoint1, crossoverPoint2 = crossoverPoint2, crossoverPoint1

            #For each box that needs to be crossed over...
            for x in range(crossoverPoint1, crossoverPoint2):
                #...Call crossoverBoxes with x as a box number
                temp1, temp2 = self.crossoverBoxes(child1, child2, x)
                #Add changes made to boards to each of the child Candidates
                child1.values = np.copy(temp1)
                child2.values = np.copy(temp2)
        
        return child1, child2




    def crossoverBoxes(self, parent1, parent2, boxNum):
        """ Takes 2 parents and a box number for each and swaps the boxes from one to another """

        #Initialise new Parents
        newParent1 = Candidate(parent1.originalPuzzle)
        newParent2 = Candidate(parent2.originalPuzzle)

        newParent1.values = np.copy(parent1.values)
        newParent2.values = np.copy(parent2.values)

        #Get box coords wanting to be swapped
        boxCoords = newParent1.getBox(boxNum)
        print("BoxCoords: ", boxCoords)

        #Get list of cells in box that are not in original board and can be changed
        changeableCells = [i for i in boxCoords if newParent1.originalPuzzle[i[0]][i[1]] == 0]

        print("Changeable cells: ", changeableCells)

        #For each coordinate that is changeable...
        for coord in changeableCells:
            #...swap the cell from one candidate to another
            newParent1.values[coord[0]][coord[1]], newParent2.values[coord[0]][coord[1]] = newParent2.values[coord[0]][coord[1]] , newParent1.values[coord[0]][coord[1]]


        return newParent1.values, newParent2.values


class Sudoku:
    
    def __init__(self, puzzle):
        self.originalPuzzle = puzzle
        self.counter = 0
    
    def solve(self):

        #Initialisations
        Nc = 100  # Number of candidates (i.e. population size).
        Ne = int(0.05*Nc)  # Number of elites.
        Ng = 1000  # Number of generations.
        Nm = 0  # Number of mutations.

        # Mutation parameters.
        phi = 0
        sigma = 1
        mutationRate = 0.06

        #Initialise the population
        self.population = Population()
        self.population.intialise(Nc, self.originalPuzzle)

        stale = 0
        #For each generation...
        for generation in range(Ng):
            
            print("Generation: ", generation+1)


            #Find best fitness in population
            bestFitness = self.population.candidates[0].fitness

            #For each candidate in the population...
            for candidate in self.population.candidates:

                #Check for solution by checking fitness equals 0 (e.g no errors in solution)
                if(candidate.fitness == 0):
                    print("Solution Found")
                    print(candidate.values)
                    #If solution found, return solution
                    return candidate

                if(candidate.fitness < bestFitness):
                    bestFitness = candidate.fitness
            
            print("Best Fitness: ", bestFitness)

            nextPopulation = []

            #Sort population and get best fitness candidates
            self.population.sort()

            bestCandidates = []
            for candidate in range(Ne):
                bestCandidates.append(self.population.candidates[candidate])

            #Do tournament on population and crossover the parents

            for count in range(Ne, Nc, 2):
                #Select paretns from population to be crossed over
                S =  Selection()

                parent1 = S.compete(self.population.candidates)
                parent2 = S.compete(self.population.candidates)

                C = Crossover()
                child1, child2 = C.crossover(parent1, parent2, 1.0)


                #Mutate the child candidates from the crossover

                child1.mutate(mutationRate)

                child2.mutate(mutationRate)

                #Add new candidates to the population

                nextPopulation.append(child1)
                nextPopulation.append(child2)

            for candidate in bestCandidates:
                nextPopulation.append(candidate)
                
            #update fitnesses for new population
            self.population.candidates = nextPopulation
            self.population.updateFitnesses()

            # Calculate new adaptive mutation rate (based on Rechenberg's 1/5 success rule). This is to stop too much mutation as the fitness progresses towards unity.
            if(Nm == 0):
                phi = 0  # Avoid divide by zero.
            else:
                phi = phi / Nm
            
            if(phi > 0.2):
                sigma = sigma/0.998
            elif(phi < 0.2):
                sigma = sigma*0.998

            mutationRate = abs(np.random.normal(loc=0.0, scale=sigma, size=None))

            #Do next generation
        
        print("No solution Found")
        return None




if __name__ == "__main__":

    mutation_rate = 0.06

    board = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])

    S = Sudoku(board)

    S.solve()


    # P = Population()
    # P.intialise(board)
    # C = Crossover()

    # parent1 = P.candidates[0]
    # parent2 = P.candidates[1]

    # print(parent1.values)
    # print()
    # print(parent2.values)
    # print("\n\n")

    # newParent1, newParent2 = C.crossoverBoxes(parent1, parent2, 0)

    # print(newParent1.values)
    # print()
    # print(newParent2.values)





    

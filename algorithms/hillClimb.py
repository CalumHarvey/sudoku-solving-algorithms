import random
import numpy as np

'''
Hill climb involves moving towards the correct solution each time like climbing a hill to each the top
Since it always tries to improve it can get into local minimums, this is common in sudoku so there needs to be a restart ability if too many iterations are taken.
'''


def getBox(boxNum):
    ''' Given box number from 0-8 return a list of the coordinates of the box '''
    #Get coordinate of first row and column of box number
    firstRow = (boxNum // 3) * 3
    firstCol = (boxNum % 3) * 3

    #Get list of all coordinates of the current box
    boxCoords = [[firstRow+i, firstCol+j] for i in range(3) for j in range(3)]

    return boxCoords


def intialSolution(board):
    ''' Create intial solution where numbers 1-9 are in each 3x3 box only once each '''
    populatedBoard = board.copy()
    #For each box number 1-9...
    for boxNum in range(9):
        #Get box coordinates
        boxCoords = getBox(boxNum)
        
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

    return populatedBoard


class hillClimb:
    def __init__(self, puzzle):
        self.currentState = np.zeros((9,9))
        self.solutionState = np.zeros((9,9))
        self.iterations = 0
        self.intialState = np.array(puzzle)


    def solve(self):

        while True:
            #input()
            self.iterations = 0
            self.currentState = intialSolution(self.intialState)

            solutionState = self.climb(self.currentState)
            print("out of loop")

            self.currentState = solutionState

            if(self.energy(self.currentState) == 0):
                print("run")
                break
        
        return solutionState



    def energy(self, puzzle):
        '''Calculate number of errors in solution'''
        score = 0
        #For each row 1-9...
        for x in range(9):
            #Intialise sets
            rowSet = set()
            colSet = set()
            #For each value in row...
            for y in range(9):
                #Add numbers from each row into rowSet and numbers in columns into colSet
                rowSet.add(puzzle[x][y])
                colSet.add(puzzle[y][x])
            
            #print("lenRow", len(rowSet))
            #print("lenCol", len(colSet))

            #Add to score the number of values in each row and column that is less than 9 (all the values)
            score += (9 - len(rowSet))
            score += (9 - len(colSet))       

        #if score is 0 then solution is found, exit the program

        return score


    def climb(self, oldState):

        nextState = np.copy(oldState)
            
        boxNum = random.randrange(0,8)

        boxCoords = getBox(boxNum)

        #changeableCells = [i for i in boxCoords if self.intialState[i[0]][i[1]] == 0]
        changeableCells = []
        for i in boxCoords:
            if (self.intialState[i[0]][i[1]] == 0):
                changeableCells.append(i)
        
        #Pick 2 random coordinates from the list of changeable cells
        a = random.sample(changeableCells, 1)
        b = random.sample(changeableCells, 1)
        
        #Swap values of 2 random coordinates
        #nextState[a[0]], nextState[b[0]] = nextState[b[0]] , nextState[a[0]]
        temp = nextState[a[0][0]][a[0][1]]
        nextState[a[0][0]][a[0][1]] = nextState[b[0][0]][b[0][1]]
        nextState[b[0][0]][b[0][1]] = temp

        #print("current state", self.currentState)
        #print("neighbour state", nextState)

        nextStateError = self.energy(nextState)

        currentError = self.energy(oldState)

        print("neighbour error ", nextStateError)
        print("current error ", currentError)
        print("iterations", self.iterations)
        #print(nextStateError >= currentError)
        #input()


        self.iterations += 1

        if(self.iterations == 200):
            return oldState

        if(nextStateError == 0):
            print("error 0")
            #return nextState
        elif(nextStateError >= currentError):
            #print("neighbour worse")
            return self.climb(oldState)
        else:
            #print("neighbour better")
            return self.climb(nextState)



if __name__ == "__main__":
    #board = np.array([[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]])
    #board = [[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]]

    #board = np.array([[7, 5, 6, 0, 1, 0, 0, 4, 9], [0, 0, 0, 0, 9, 4, 0, 8, 0], [0, 9, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 2, 0, 0], [3, 0, 8, 0, 2, 0, 0, 1, 5], [2, 0, 0, 9, 7, 3, 4, 6, 0], [0, 6, 0, 1, 0, 8, 0, 9, 0], [4, 8, 0, 2, 0, 0, 1, 0, 0], [9, 0, 0, 3, 0, 0, 0, 0, 0]])

    board = np.array([[0, 0, 0, 7, 0, 8, 0, 0, 3], [0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 6, 3, 4, 9, 0, 0, 5, 7], [0, 3, 1, 0, 0, 2, 0, 0, 0], [9, 0, 8, 0, 0, 7, 0, 6, 5], [6, 5, 0, 0, 0, 4, 0, 1, 0], [0, 0, 9, 0, 0, 0, 0, 0, 0], [0, 0, 6, 1, 3, 0, 0, 0, 9], [5, 0, 0, 0, 7, 0, 8, 3, 0]])
    
    a = hillClimb(board)

    solvedBoard = a.solve()

    print(solvedBoard)




             










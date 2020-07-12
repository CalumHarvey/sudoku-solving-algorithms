

import numpy as np
import random

class Candidate:
    def __init__(self):
        self.values = np.zeros((9, 9), dtype=np.int32)
        self.fitness = None
    
    def getBox(self, boxNum):
        ''' Given box number from 0-8 return a list of the coordinates of the box '''
        #Get coordinate of first row and column of box number
        firstRow = (boxNum // 3) * 3
        firstCol = (boxNum % 3) * 3

        #Get list of all coordinates of the current box
        boxCoords = [[firstRow+i, firstCol+j] for i in range(3) for j in range(3)]

        return boxCoords
    
    def initialise(self, puzzle):

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
        pass



class Population:
    def __init__(self):
        self.candidates = []
    
    def intialise(self, puzzle):
        
        for x in range(100):
            newCandidate = Candidate()
            newCandidate.initialise(puzzle)
            print(newCandidate.values)
            input()
            self.candidates.append(newCandidate)


    
    def updateFitnesses(self):
        pass

    def getBest(self):
        pass


if __name__ == "__main__":

    board = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])

    P = Population()
    P.intialise(board)


    

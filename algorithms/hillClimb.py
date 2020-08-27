import random
import numpy as np
import time
import datetime

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


def initialSolution(board):
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
        self.initialState = np.array(puzzle)
        self.passes = 0
        self.energy = 81
        self.solved = False
        self.stale = 0
        self.retries = 0


    def solve(self):

        self.currentState = initialSolution(self.initialState)

        while True:

            climbed = self.move()
            print(self.passes, ": ", self.energy)

            if(self.solved == True):
                print("Puzzle Solved")
                print("Number of passes: ", self.passes)
                print("Number of retries: ", self.retries)
                return self.currentState

            if (self.stale >= 500):
                self.currentState = initialSolution(self.initialState)
                self.stale = 0
                self.energy = 81
                self.retries += 1

            if(self.retries > 500):
                print("Solution not found - algorithm timed out")
                return self.currentState



    def getEnergy(self, puzzle):
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

            #Add to score the number of values in each row and column that is less than 9 (all the values)
            score += (9 - len(rowSet))
            score += (9 - len(colSet))       

        #if score is 0 then solution is found, exit the program

        return score


    def move(self):
        """ Select box and swap 2 non-fixed cells within the box """

        climbed = False

        while True:
            nextState = np.copy(self.currentState)
            
            boxNum = random.randrange(0,8)

            boxCoords = getBox(boxNum)

            #changeableCells = [i for i in boxCoords if self.intialState[i[0]][i[1]] == 0]
            changeableCells = []
            for i in boxCoords:
             if (self.initialState[i[0]][i[1]] == 0):
                    changeableCells.append(i)
                
            if(len(changeableCells) >= 2):
                break
        
        #Pick 2 random coordinates from the list of changeable cells
        a = random.sample(changeableCells, 1)
        b = random.sample(changeableCells, 1)
        
        #Swap values of 2 random coordinates
        temp = nextState[a[0][0]][a[0][1]]
        nextState[a[0][0]][a[0][1]] = nextState[b[0][0]][b[0][1]]
        nextState[b[0][0]][b[0][1]] = temp


        nextStateError = self.getEnergy(nextState)

        currentError = self.energy


        self.passes += 1

        if(nextStateError == 0):
            self.currentState = nextState
            self.solved = True
        
        elif(nextStateError < currentError):
            self.currentState = nextState
            self.energy = nextStateError
            climbed = True
            self.stale = 0
        
        else:
            self.stale += 1


        return climbed 

def runAlgorithm(board):
    a = hillClimb(np.array(board))

    start = datetime.datetime.now()

    solvedBoard = a.solve()

    end = datetime.datetime.now()

    #Calculate the time taken for the algorithm to run
    timeTaken = end - start

    #Change timer to show seconds
    timeOutput = (timeTaken.total_seconds())

    return timeOutput, a.passes

def testing(board):
    a = hillClimb(board)
    solvedBoard = a.solve()

    return solvedBoard


if __name__ == "__main__":

    board = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])

    
    
    
    
    board2 = np.array([[9, 0, 0, 3, 0, 2, 0, 0, 6], [8, 0, 0, 5, 9, 0, 1, 0, 2], [6, 1, 0, 8, 0, 4, 0, 9, 5], [5, 8, 3, 2, 0, 9, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 5, 0], [0, 6, 9, 0, 0, 0, 2, 0, 0], [0, 0, 7, 9, 0, 1, 0, 0, 0], [1, 0, 0, 0, 2, 5, 0, 0, 0], [0, 5, 0, 4, 3, 0, 0, 0, 0]])

    board3 = np.array([
        [0, 2, 8, 0, 9, 0, 7, 3, 0], 
        [0, 0, 5, 8, 1, 7, 0, 0, 0], 
        [6, 0, 0, 2, 0, 0, 9, 0, 0], 
        [3, 0, 2, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 5, 8, 2, 6, 0], 
        [0, 0, 0, 0, 0, 0, 8, 7, 0], 
        [2, 5, 3, 7, 0, 0, 4, 9, 0], 
        [7, 0, 6, 0, 0, 0, 0, 0, 2], 
        [8, 9, 0, 5, 0, 2, 3, 0, 0]])



    a = hillClimb(board2)

    solvedBoard = a.solve()

    print(solvedBoard)





             










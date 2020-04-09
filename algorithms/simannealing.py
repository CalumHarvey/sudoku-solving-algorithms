import random
import numpy as np
from simanneal import Annealer
import datetime

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

class SudokuSolve(Annealer):
    ''' Initialisation of sudoku solver for Simulated Annealing '''
    def __init__(self, board):
        self.board = board
        self.counter = 0
        
        #Get intial solution
        state = intialSolution(board)
        
        #call super class of simulated annealing
        super().__init__(state)

    def move(self):
        '''Swap 2 cells within a single 3x3 box randomly'''

        #Get random box number and get list of coordinates in that box
        boxNum = random.randrange(9)
        boxCoords = getBox(boxNum)

        #Get list of cells in box that are not in original board and can be changed
        changeableCells = [i for i in boxCoords if self.board[i[0]][i[1]] == 0]
        
        #Pick 2 random coordinates from the list of changeable cells
        a = random.sample(changeableCells, 1)
        b = random.sample(changeableCells, 1)
        
        #Swap values of 2 random coordinates
        self.state[a[0][0]][a[0][1]], self.state[b[0][0]][b[0][1]] = self.state[b[0][0]][b[0][1]] , self.state[a[0][0]][a[0][1]]
        self.counter += 1

    def energy(self):
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
                rowSet.add(self.state[x][y])
                colSet.add(self.state[y][x])

            #Add to score the number of values in each row and column that is less than 9 (all the values)
            score += (9 - len(rowSet))
            score += (9 - len(colSet))       

        #if score is 0 then solution is found, exit the program
        if(score == 0):
            self.user_exit = True

        return score

def runAlgorithm(board):
    ''' Initialise and run algorithm for Simulated Annealing ''' 

    boardNew = np.copy(board)

    sudoku = SudokuSolve(boardNew)
    sudoku.counter = 0
    
    sudoku.copy_strategy = "method"

    #Initialise the variables for simulated annealing
    sudoku.Tmax = 0.5
    sudoku.Tmin = 0.05
    sudoku.steps = 700000
    sudoku.updates = 1000

    #Start timer 
    start = datetime.datetime.now()
    #Run algorithm
    state, e = sudoku.anneal()
    #End timer
    end = datetime.datetime.now()

    #Calculated time taken for algorithm to run
    timeTaken = end - start

    #Turn time time taken into seconds
    timeOutput = (timeTaken.total_seconds())

    #Return tuple of time taken and the number of passes
    return timeOutput, sudoku.counter


if __name__ == "__main__":
    #board = np.array([[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]])
    #board = [[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]]

    #board = np.array([[7, 5, 6, 0, 1, 0, 0, 4, 9], [0, 0, 0, 0, 9, 4, 0, 8, 0], [0, 9, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 2, 0, 0], [3, 0, 8, 0, 2, 0, 0, 1, 5], [2, 0, 0, 9, 7, 3, 4, 6, 0], [0, 6, 0, 1, 0, 8, 0, 9, 0], [4, 8, 0, 2, 0, 0, 1, 0, 0], [9, 0, 0, 3, 0, 0, 0, 0, 0]])

    board = np.array([[0, 0, 0, 7, 0, 8, 0, 0, 3], [0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 6, 3, 4, 9, 0, 0, 5, 7], [0, 3, 1, 0, 0, 2, 0, 0, 0], [9, 0, 8, 0, 0, 7, 0, 6, 5], [6, 5, 0, 0, 0, 4, 0, 1, 0], [0, 0, 9, 0, 0, 0, 0, 0, 0], [0, 0, 6, 1, 3, 0, 0, 0, 9], [5, 0, 0, 0, 7, 0, 8, 3, 0]])

    print(board)
    
    runAlgorithm(board)
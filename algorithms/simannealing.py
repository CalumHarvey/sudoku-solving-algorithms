# Simulated Annealing
import random
import numpy as np
from simanneal import Annealer
import datetime

# Given box number from 0-8 return the a list of the coordinates of the box  
def getBox(boxNum):
    
    firstRow = (boxNum // 3) * 3
    firstCol = (boxNum % 3) * 3

    boxCoords = [[firstRow+i, firstCol+j] for i in range(3) for j in range(3)]

    return boxCoords

'''
Create intial solution where numbers 1-9 are in each 3x3 box only once each 
'''
def intialSolution(board):
    populatedBoard = board.copy()
    for boxNum in range(9):
        boxCoords = getBox(boxNum)
        
        valuesCoords = [i for i in boxCoords if populatedBoard[i[0]][i[1]] != 0]
        values = [populatedBoard[i[0]][i[1]] for i in valuesCoords]

        zeroCoords = [i for i in boxCoords if populatedBoard[i[0]][i[1]] == 0]
        toFillValues = [i for i in range(1,10) if i not in values]
        random.shuffle(toFillValues)
        fillCounter = 0
        for x in zeroCoords:
            populatedBoard[x[0]][x[1]] = toFillValues[fillCounter]
            fillCounter += 1

    return populatedBoard

class SudokuSolve(Annealer):
    def __init__(self, board):
        self.board = board
        self.counter = 0
        state = intialSolution(board)
        super().__init__(state)

    '''Swap 2 cells within a single 3x3 box randomly'''
    def move(self):
        boxNum = random.randrange(9)
        boxCoords = getBox(boxNum)
        changeableCells = [i for i in boxCoords if self.board[i[0]][i[1]] == 0]
        a = random.sample(changeableCells, 1)
        b = random.sample(changeableCells, 1)
        self.state[a[0][0]][a[0][1]], self.state[b[0][0]][b[0][1]] = self.state[b[0][0]][b[0][1]] , self.state[a[0][0]][a[0][1]]
        #self.state[tuple(a)], self.state[tuple(b)] = self.state[tuple(b)] , self.state[tuple(a)]
        self.counter += 1

    '''Calculate number of errors in solution'''
    def energy(self):
        score = 0
        for x in range(9):
            rowSet = set()
            colSet = set()
            for y in range(9):
                rowSet.add(self.state[x][y])
                colSet.add(self.state[y][x])

            score += (9 - len(rowSet))
            score += (9 - len(colSet))       

        if(score == 0):
            self.user_exit = True

        return score

def runAlgorithm(board):
    
    boardNew = np.copy(board)

    sudoku = SudokuSolve(boardNew)
    sudoku.copy_strategy = "method"

    sudoku.Tmax = 0.5
    sudoku.Tmin = 0.05
    sudoku.steps = 700000
    sudoku.updates = 1000

    start = datetime.datetime.now()
    state, e = sudoku.anneal()
    end = datetime.datetime.now()

    timeTaken = end - start

    timeOutput = (timeTaken.total_seconds())

    return timeOutput, sudoku.counter


if __name__ == "__main__":
    #board = np.array([[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]])
    #board = [[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]]

    #board = np.array([[7, 5, 6, 0, 1, 0, 0, 4, 9], [0, 0, 0, 0, 9, 4, 0, 8, 0], [0, 9, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 2, 0, 0], [3, 0, 8, 0, 2, 0, 0, 1, 5], [2, 0, 0, 9, 7, 3, 4, 6, 0], [0, 6, 0, 1, 0, 8, 0, 9, 0], [4, 8, 0, 2, 0, 0, 1, 0, 0], [9, 0, 0, 3, 0, 0, 0, 0, 0]])

    board = np.array([[0, 0, 0, 7, 0, 8, 0, 0, 3], [0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 6, 3, 4, 9, 0, 0, 5, 7], [0, 3, 1, 0, 0, 2, 0, 0, 0], [9, 0, 8, 0, 0, 7, 0, 6, 5], [6, 5, 0, 0, 0, 4, 0, 1, 0], [0, 0, 9, 0, 0, 0, 0, 0, 0], [0, 0, 6, 1, 3, 0, 0, 0, 9], [5, 0, 0, 0, 7, 0, 8, 3, 0]])

    print(board)
    
    runAlgorithm(board)
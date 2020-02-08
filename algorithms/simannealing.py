# Simulated Annealing
import random
import numpy as np
from simanneal import Annealer


board = [[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]]

'''
get initial solution - 1-9 in each 3x3 box: can then check rows and columns to ensure correct solution
get intial temperature
loop end 2
loop start
generate neighbouring solution
check intial solution cost vs neighbouring solution cost
swap if new solution is better or if worse but temperature high enough
loop end

reduce temperature and loop start 2
'''
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
        state = intialSolution(board)
        super().__init__(state)

    '''Swap 2 cells within a single 3x3 box randomly'''
    def move(self):
        boxNum = random.randrange(9)
        boxCoords = getBox(boxNum)
        changeableCells = [i for i in boxCoords if board[i[0]][i[1]] == 0]
        a = random.sample(changeableCells, 1)
        b = random.sample(changeableCells, 1)
        self.state[a[0][0]][a[0][1]], self.state[b[0][0]][b[0][1]] = self.state[b[0][0]][b[0][1]] , self.state[a[0][0]][a[0][1]]

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

def runAlgorithm():
    board = np.array([[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]])
    sudoku = SudokuSolve(board)
    sudoku.copy_strategy = "method"

    #sudoku.steps = 1000000
    #auto_schedule = sudoku.auto(minutes=1)
    #print(auto_schedule)
    #sudoku.set_schedule(auto_schedule)


    sudoku.Tmax = 5
    sudoku.Tmin = 0.05
    sudoku.steps = 10000
    sudoku.updates = 100

    #print(sudoku.board)

    state, e = sudoku.anneal()

    print()
    print(state)
    print(e)




if __name__ == "__main__":
    
    runAlgorithm()

    


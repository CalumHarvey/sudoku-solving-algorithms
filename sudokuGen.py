
'''
1. Create valid completed board
2. By selecting difficulty - chooses number of numbers to remove
    easy = 10, medium = 20, hard = 30
3. removes that number of cells, checking that there is only one solution
    remove cell, check one solution
4. when multiple solutions, but cell back and return puzzle

'''

import time
import datetime
import random
import numpy as np

counter = 0


def findUnassignedLocation(board, pos):
    for row in range(9):
        for col in range(9):
            if(board[row][col] == 0):
                pos[0] = row
                pos[1] = col
                return True
    return False


def noConflicts(board, pos, num):

    return not usedInRow(board, pos[0], num) and not usedInCol(board, pos[1], num) and not usedInBox(board, pos[0] - pos[0] % 3, pos[1]-pos[1] % 3, num)


def usedInRow(board, row, num):
    for col in range(9):
        if(board[row][col] == num):
            return True
    return False


def usedInCol(board, col, num):
    for row in range(9):
        if(board[row][col] == num):
            return True
    return False


def usedInBox(board, boxStartRow, boxStartCol, num):
    for row in range(3):
        for col in range(3):
            if(board[row+boxStartRow][col+boxStartCol] == num):
                return True
    return False


def solveSudoku(board, start, end):

    pos = [0, 0]

    if(not findUnassignedLocation(board, pos)):
        # print("solution Found")
        return True

    # might need this
    row = pos[0]
    col = pos[1]

    for num in range(start, end):
        if(noConflicts(board, pos, num)):
            board[row][col] = num

            if(solveSudoku(board, start, end)):
                # print("solution Found 2")
                return True

            board[row][col] = 0

    return False


def fillSudoku(board):

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    pos = [0, 0]

    if(not findUnassignedLocation(board, pos)):
        return True

    # might need this
    row = pos[0]
    col = pos[1]

    for num in numbers:
        if(noConflicts(board, pos, num)):
            board[row][col] = num

            if(fillSudoku(board)):
                return True

            board[row][col] = 0

    return False


def difficultySelection(difficulty):
    cellsToRemove = 0
    if(difficulty == "1"):
        cellsToRemove = 10
    elif(difficulty == "2"):
        cellsToRemove = 20
    else:
        cellsToRemove = 30

    return cellsToRemove


def selectEmptyCell(grid):
    row = random.randint(0, 8)
    col = random.randint(0, 8)

    while(grid[row][col] == 0):
        row = random.randint(0, 8)
        col = random.randint(0, 8)

    return row, col


def main(grid):
    attempts = 5

    while(attempts > 0):

        copyGrid1 = []
        copyGrid2 = []
        gridCopy = []

        #Select a random non-empty cell from the board and set it to zero, storing the number as a backup
        coords = selectEmptyCell(grid)
        backup = grid[coords[0]][coords[1]]
        grid[coords[0]][coords[1]] = 0


        print("coords" , coords)
        print(grid[coords[0]][coords[1]])
        print("Grid\n", grid)

        #Create copy of the grid and try and solve the puzzle
        copyGrid1 = grid.copy()
        print("grid1", grid)
        copyGrid2 = grid.copy()
        print("grid2", grid)
        gridCopy = grid.copy()
        print("grid3", gridCopy)
        solvedAsc = solveSudoku(copyGrid1, 1, 10)
        print("grid4", gridCopy)
        solvedDesc = solveSudoku(copyGrid2, 10, 1)
        print("grid5", gridCopy)
        


        #print(solvedAsc)
        #print("copygrid1\n" , copyGrid1)
        #print(solvedDesc)
        #print("copygrid2\n", copyGrid2)
        #print(np.array_equal(copyGrid1, copyGrid2))
        #input()


        if(not np.array_equal(copyGrid1, copyGrid2)):
            #print("run")
            grid[coords[0]][coords[1]] = backup
            attempts -= 1

        #Grid at end is completed but shouldnt be 
        print("grid at end\n" , grid)

        input()
    return grid



def runAlgorithm():

    grid = []
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


    fillSudoku(grid)


    finishedGrid = main(grid)

    print(finishedGrid)

    # timetaken returns 0 - algorithm too quick
    # number of passes returns 0 ????


if __name__ == "__main__":
    
    runAlgorithm()






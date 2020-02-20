
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

def findUnassignedLocation(board, pos):
    for row in range(9):
        for col in range(9):
            if(board[row][col] == 0):
                pos[0] = row
                pos[1] = col
                return True
    return False

def noConflicts(board, pos, num):

    return not usedInRow(board, pos[0], num) and not usedInCol(board, pos[1], num) and not usedInBox(board, pos[0] - pos[0]%3, pos[1]-pos[1]%3, num)


def usedInRow(board, row, num):
    for col in range(9):
        if(board[row][col] == num):
            return True
    return False

def usedInCol(board, col,num):
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

def solveSudoku(board, counter):

    pos = [0,0]
    
    if(not findUnassignedLocation(board, pos)):
        print("solution Found")
        counter += 1
        return True

    #might need this
    row = pos[0]
    col = pos[1]
    
    for num in range(9):
        if(noConflicts(board, pos, num)):
            board[row][col] = num

            if(solveSudoku(board,counter)):
                print("solution Found 2")
                counter += 1
                return True
            
            board[row][col] = 0
    
    return False


def fillSudoku(board):

    numbers = [1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)

    pos = [0,0]
    
    if(not findUnassignedLocation(board, pos)):
        return True

    #might need this
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
    elif(difficulty ==  "2"):
        cellsToRemove = 20
    else:
        cellsToRemove = 30
    
    return cellsToRemove


def selectEmptyCell(grid):
    row = random.randint(0,8)
    col = random.randint(0,8)

    while(grid[row][col] == 0):
        row = random.randint(0,8)
        col = random.randint(0,8)
     
    return row,col

def main(grid):
    attempts = 5
    counter = 0

    while attempts > 0:

        coords = selectEmptyCell(grid)
        backup = grid[coords[0]][coords[1]]

        print("coords", coords)
        print("before", grid)

        grid[coords[0]][coords[1]] = 0
        print("\n")

        print("after", grid)
        input()

        copyGrid = []
        for r in range(0,9):
            copyGrid.append([])
            for c in range(0,9):
                copyGrid[r].append(grid[r][c])
    
        solveSudoku(copyGrid,counter)

        print(counter)

        if(counter != 1):
            grid[coords[0]][coords[1]] = backup
            attempts -= 1

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

    #timetaken returns 0 - algorithm too quick
    #number of passes returns 0 ????


if __name__ == "__main__":
    
    runAlgorithm()






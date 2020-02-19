'''
Initial design is to have preset puzzles at different difficulties
difficulty can then be chosen and a random puzzle of that difficulty is chosen by the program
'''

difficultiesDict = {"1" : "easy", "2" : "medium", "3" : "hard"}

import random
import os


currentDir = os.path.dirname(__file__)

def boardPicker(difficulty):
    finalBoard = []
    
    #lineNumber = random.randint(0,3)
    lineNumber = 0 #remove when all boards implemented
    filePath = "puzzles/" + difficultiesDict[difficulty] + ".txt"
    absFilePath = os.path.join(currentDir, filePath)

    f = open(absFilePath, "r")
    allLines = f.readlines()
    line = allLines[lineNumber]

    lineStripped = line.strip()
    firstSplit = lineStripped.split(",")

    for x in firstSplit:
        splitDone = list(map(int, x.split(" ")))
        finalBoard.append(splitDone)
    
    return finalBoard

boardPicker("1")

'''

BREAK
1. Create valid completed board
2. By selecting difficulty - chooses number of numbers to remove
3. removes that number of cells, checking that there is only one solution
4. when multiple solutions, but cell back and return puzzle



'''

import time
import datetime

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

def solveSudoku(board):

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

            if(solveSudoku(board)):
                return True
            
            board[row][col] = 0
    
    return False

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

    returned = solveSudoku(grid)

    print(grid)

    #timetaken returns 0 - algorithm too quick
    #number of passes returns 0 ????

    return returned


if __name__ == "__main__":
    
    runAlgorithm()






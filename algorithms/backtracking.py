import time
import datetime
import numpy as np


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


def solveSudoku(board):

    pos = [0, 0]

    if(not findUnassignedLocation(board, pos)):
        return True

    # might need this
    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
        if(noConflicts(board, pos, num)):
            board[row][col] = num

            if(solveSudoku(board)):
                return True

            board[row][col] = 0

    solveSudoku.counter += 1
    return False


def runAlgorithm(board):
    solveSudoku.counter = 0
    newBoard = np.array(board)

    start = datetime.datetime.now()
    returned = solveSudoku(newBoard)
    end = datetime.datetime.now()

    #startString = start.strftime("%f")
    #endString = end.strftime("%f")

    timeTaken = end - start
    #(format(timeTaken, ',d'))
    timeOutput = (timeTaken.total_seconds())

    return timeOutput, solveSudoku.counter


if __name__ == "__main__":
    board = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])
    runAlgorithm(board)

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
        print("true1")
        return True

    # might need this
    row = pos[0]
    col = pos[1]

    for num in range(1, 10):
        if(noConflicts(board, pos, num)):
            board[row][col] = num

            if(solveSudoku(board)):
                print("true2")
                return True

            board[row][col] = 0

    solveSudoku.counter += 1
    return False


def runAlgorithm(board):
    solveSudoku.counter = 0
    start = datetime.datetime.now()
    returned = solveSudoku(board)
    end = datetime.datetime.now()

    timeTaken = end - start

    print(returned)
    print(board)

    # timetaken returns 0 - algorithm too quick
    # number of passes returns 0 ????

    return timeTaken, solveSudoku.counter


if __name__ == "__main__":
    board = np.array([[0, 0, 2, 1, 0, 0, 0, 0, 0], [7, 1, 0, 6, 0, 0, 0, 4, 0], [5, 0, 0, 9, 0, 3, 0, 0, 1], [2, 0, 0, 8, 0, 0, 0, 9, 3], [
                     0, 8, 0, 0, 0, 0, 0, 1, 0], [9, 5, 0, 0, 0, 1, 0, 0, 4], [3, 0, 0, 4, 0, 9, 0, 0, 8], [0, 9, 0, 0, 0, 2, 0, 7, 6], [0, 0, 0, 0, 0, 7, 4, 0, 0]])
    runAlgorithm(board)

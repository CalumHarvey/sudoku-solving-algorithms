import time
import datetime
import numpy as np


class backtracking:
    def __init__(self, board):
        self.counter = 0
        self.board = board


    def findUnassignedLocation(self, board, pos):
         #Inputs: puzzle board, position - x,y coordinations
        #Loops through each number looking for an zero
        #Returns true if finds one, else false
        for row in range(9):
            for col in range(9):
                if(self.board[row][col] == 0):
                    pos[0] = row
                    pos[1] = col
                    return True
        return False


    def noConflicts(self, board, pos, num):
        #Inputs: puzzle board, current position - x,y coordinates, number trying to be added
        #Checks if num is already used in the row, column and box

        return not self.usedInRow(board, pos[0], num) and not self.usedInCol(board, pos[1], num) and not self.usedInBox(board, pos[0] - pos[0] % 3, pos[1]-pos[1] % 3, num)


    def usedInRow(self, board, row, num):
        #Input: puzzle board, current row, number trying to be added
        #Checks each number in the row for the number trying to be added
        for col in range(9):
            if(self.board[row][col] == num):
                return True
        return False


    def usedInCol(self, board, col, num):
        #Inputs: puzzle board, current column, number trying to be added
        #Checks each number in the column for the number trying to be added
        for row in range(9):
            if(self.board[row][col] == num):
                return True
        return  False


    def usedInBox(self, board, boxStartRow, boxStartCol, num):
        #Input: puzzle board, coordinate of the start of the 3x3 box, number trying to be added
        #Checks each number in the 3x3 box for the number trying to be added
        for row in range(3):
            for col in range(3):
                if(self.board[row+boxStartRow][col+boxStartCol] == num):
                    return True
        return False


    def solveSudoku(self, board):
        #Inputs: the grid that needs to be solved
        #Solves the puzzle using recursive backtracking

        #Initial start at coordinates 0,0
        pos = [0, 0]

        if(not self.findUnassignedLocation(board, pos)):
            #Look for an empty location (a zero)
            #Base case for the recursion
            return True

        #Set current row and column
        row = pos[0]
        col = pos[1]

        for num in range(1, 10):
            #Check through the numbers 1-9
            if(self.noConflicts(board, pos, num)):
                #Check for conflict with the current number and current coordinates
                #Set current row and column position to the current number
                board[row][col] = num

                if(self.solveSudoku(board)):
                    #Recursively call solveSudoku with the new updated board
                    return True

                #If it doesn't work, set back to 0
                self.board[row][col] = 0

        #Increment pass counter after each pass
        self.counter += 1
        return False


def runAlgorithm(board):
    #Input: board to be solved

    #Turn input board into a numpy array
    newBoard = np.array(board)

    sudoku = backtracking(newBoard)
    
    #Initalise passes counter
    #solveSudoku.counter = 0
    sudoku.counter = 0

    #Take the time before and after the solve algorithm is run
    start = datetime.datetime.now()
    returned = sudoku.solveSudoku(newBoard)
    end = datetime.datetime.now()

    #Calculate the time taken for the algorithm to run
    timeTaken = end - start

    #Change timer to show seconds
    timeOutput = (timeTaken.total_seconds())

    #Return a tuple of the time taken and the number of passes
    return timeOutput, sudoku.counter


if __name__ == "__main__":
    board = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])
    results = runAlgorithm(board)

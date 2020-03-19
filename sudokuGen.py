
import time
import datetime
import random
import numpy as np
import copy
import os


class sudokuGen:
    def __init__(self, grid):
        #Object intialisation
        #Input: empty 9x9 grid
        self.grid = grid



    def findUnassignedLocation(self, board, pos):
        #Inputs: puzzle board, position - x,y coordinations
        #Loops through each number looking for an zero
        #Returns true if finds one, else false
        for row in range(9):
            for col in range(9):
                if(board[row][col] == 0):
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
            if(board[row][col] == num):
                return True
        return False


    def usedInCol(self, board, col, num):
        #Inputs: puzzle board, current column, number trying to be added
        #Checks each number in the column for the number trying to be added
        for row in range(9):
            if(board[row][col] == num):
             return True
        return False


    def usedInBox(self, board, boxStartRow, boxStartCol, num):
        #Input: puzzle board, coordinate of the start of the 3x3 box, number trying to be added
        #Checks each number in the 3x3 box for the number trying to be added
        for row in range(3):
            for col in range(3):
                if(board[row+boxStartRow][col+boxStartCol] == num):
                    return True
        return False


    def solveSudoku(self, board, nums):
        #Inputs: puzzle board, list of numbers either 1-9 or 9-1 used to solve the puzzle
        #Solves the board given using backtracking

        pos = [0, 0]

        if(not self.findUnassignedLocation(board, pos)):
            #Base case for recursion
            #Check for zeros in the puzzle, if no zeros return true
            return True

        #set positions of current row and column
        row = pos[0]
        col = pos[1]

        for num in nums:
        #for each number in the list passed into the function
            if(self.noConflicts(board, pos, num)):
                #Check if there are conflicts with current number
                board[row][col] = num

                if(self.solveSudoku(board, nums)):
                    #recursive call with added number 
                    return True

                board[row][col] = 0
                #If fails check, set back to zero

        return False


    def fillSudoku(self, board):
        #Inputs: empty 9x9 grid

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        #Randomly shuffles numbers 1-9 in a list

        pos = [0, 0]

        if(not self.findUnassignedLocation(board, pos)):
            #Recursive base case
            #Checks for non-zero elements
            return True

        #Sets current row and column
        row = pos[0]
        col = pos[1]

        for num in numbers:
            #Loop for each number in random list
            if(self.noConflicts(board, pos, num)):
                #Check for no conflicts with current number
                board[row][col] = num

                if(self.fillSudoku(board)):
                    #recursive call with updated board
                    return True

                board[row][col] = 0

        return False


    def selectEmptyCell(self, grid):
        #Inputs: sudoku grid
        #Finds random non empty cell in grid (find not zero in list)

        #Row and column are random numbers between 0 and 8
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        while(grid[row][col] == 0):
            #While row and column are not zero, try again
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        #Return non empty coordinates
        return row, col


    def main(self, grid):
        #Inputs: empty sudoku grid

        #Number of attempts to remove an element from the grid
        attempts = 5
        asc = [1,2,3,4,5,6,7,8,9]
        desc = [9,8,7,6,5,4,3,2,1]

        while(attempts > 0):
            #While attempts is greater than 0

            copyGrid1 = []
            copyGrid2 = []

            #Select a random non-empty cell from the board and set it to zero, storing the number as a backup
            coords = self.selectEmptyCell(grid)
            backup = grid[coords[0]][coords[1]]
            grid[coords[0]][coords[1]] = 0

            #Create copy of the grid and try and solve the puzzle
            copyGrid1 = copy.deepcopy(grid)
            copyGrid2 = copy.deepcopy(grid)
            #Try solve using numbers 1-9 and 9-1
            self.solveSudoku(copyGrid1, asc)
            self.solveSudoku(copyGrid2,desc)

            if(not np.array_equal(copyGrid1, copyGrid2)):
                #If the 2 solves find different solutions then there are multiple solutions to the puzzle
                #Therefore, put the number that was removed back and try again
                #Reducing attempts by 1
                grid[coords[0]][coords[1]] = backup
                attempts -= 1

        #Return grid to be solved with numbers removed
        return grid



def runAlgorithm(numPuzzles):
    #Inputs: number of puzzles that needs to be created
    global x
    x=0

    boards = []

    cur_path = os.path.dirname(__file__)
    rel_path = "puzzles/puzzles.txt"
    abs_file_path = os.path.join(cur_path, rel_path)

    for x in range(numPuzzles):
        #Loop for the number of puzzles being created

        print(x)

        #Create empty 9x9 grid
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

        #Intialise Object with empty grid
        s = sudokuGen(grid)
        #Populated grid with valid final solution
        s.fillSudoku(grid)
        #Run main to remove numbers
        finishedGrid = s.main(grid)

        # 2d array into long string to write in text file
        gridSplit = [y for x in finishedGrid for y in x]
        stringGrid = ",".join(map(str,gridSplit))

        #Add board string to an array of all boards
        boards.append(stringGrid)

    #Write all the boards to file, each board is on a separate line
    f = open(abs_file_path, "w")
    for line in boards:
        f.write(line + "\n")
    f.close()



if __name__ == "__main__":
    
    runAlgorithm()






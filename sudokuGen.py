
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
import copy
import os


class sudokuGen:
    def __init__(self, grid):
        self.grid = grid



    def findUnassignedLocation(self, board, pos):
        for row in range(9):
            for col in range(9):
                if(board[row][col] == 0):
                    pos[0] = row
                    pos[1] = col
                    return True
        return False


    def noConflicts(self, board, pos, num):

        return not self.usedInRow(board, pos[0], num) and not self.usedInCol(board, pos[1], num) and not self.usedInBox(board, pos[0] - pos[0] % 3, pos[1]-pos[1] % 3, num)


    def usedInRow(self, board, row, num):
        for col in range(9):
            if(board[row][col] == num):
                return True
        return False


    def usedInCol(self, board, col, num):
        for row in range(9):
            if(board[row][col] == num):
             return True
        return False


    def usedInBox(self, board, boxStartRow, boxStartCol, num):
        for row in range(3):
            for col in range(3):
                if(board[row+boxStartRow][col+boxStartCol] == num):
                    return True
        return False


    def solveSudoku(self, board, nums):

        pos = [0, 0]

        if(not self.findUnassignedLocation(board, pos)):
            return True

        # might need this
        row = pos[0]
        col = pos[1]

        for num in nums:
            if(self.noConflicts(board, pos, num)):
                board[row][col] = num

                if(self.solveSudoku(board, nums)):
                    return True

                board[row][col] = 0

        return False


    def fillSudoku(self, board):

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)

        pos = [0, 0]

        if(not self.findUnassignedLocation(board, pos)):
            return True

        # might need this
        row = pos[0]
        col = pos[1]

        for num in numbers:
            if(self.noConflicts(board, pos, num)):
                board[row][col] = num

                if(self.fillSudoku(board)):
                    return True

                board[row][col] = 0

        return False


    def difficultySelection(self, difficulty):
        cellsToRemove = 0
        if(difficulty == "1"):
            cellsToRemove = 10
        elif(difficulty == "2"):
            cellsToRemove = 20
        else:
            cellsToRemove = 30

        return cellsToRemove


    def selectEmptyCell(self, grid):
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        while(grid[row][col] == 0):
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        return row, col


    def main(self, grid):

        attempts = 5
        asc = [1,2,3,4,5,6,7,8,9]
        desc = [9,8,7,6,5,4,3,2,1]

        while(attempts > 0):

            copyGrid1 = []
            copyGrid2 = []

            #Select a random non-empty cell from the board and set it to zero, storing the number as a backup
            coords = self.selectEmptyCell(grid)
            backup = grid[coords[0]][coords[1]]
            grid[coords[0]][coords[1]] = 0

            #Create copy of the grid and try and solve the puzzle
            copyGrid1 = copy.deepcopy(grid)
            copyGrid2 = copy.deepcopy(grid)
            self.solveSudoku(copyGrid1, asc)
            self.solveSudoku(copyGrid2,desc)

            if(not np.array_equal(copyGrid1, copyGrid2)):
                grid[coords[0]][coords[1]] = backup
                attempts -= 1

        return grid



def runAlgorithm(numPuzzles):
    global x
    x=0

    boards = []

    cur_path = os.path.dirname(__file__)
    rel_path = "puzzles/puzzles.txt"
    abs_file_path = os.path.join(cur_path, rel_path)

    for x in range(numPuzzles):


        print(x)

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

        s = sudokuGen(grid)
        s.fillSudoku(grid)
        finishedGrid = s.main(grid)

        # 2d array into long string to stop in text file
        gridSplit = [y for x in finishedGrid for y in x]
        stringGrid = ",".join(map(str,gridSplit))

        boards.append(stringGrid)

    f = open(abs_file_path, "w")
    for line in boards:
        f.write(line + "\n")
    f.close()



if __name__ == "__main__":
    
    runAlgorithm()






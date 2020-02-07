# Simulated Annealing
import random

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

    boxValues = [(firstRow+i, firstCol+j) for i in range(3) for j in range(3)]
    print(boxValues)
    return boxValues

#def intialSolution(board):
#    for x in range(0,9,3):


def intialSolution(board):
    for row in board:
        permu = [n for n in range(1,10) if n not in row]
        random.shuffle(permu)
        permuCounter = 0
        for x in range(9):
            if row[x] == 0:
                row[x] = permu[permuCounter]
                permuCounter += 1


if __name__ == "__main__":
    getBox(3)
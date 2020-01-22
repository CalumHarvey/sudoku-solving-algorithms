

def findUnassignedLocation(board, pos):
    for row in range(9):
        for col in range(9):
            if(board[row, col] == 0):
                pos[0] = row
                pos[1] = col
                return True
    return False

def noConflicts(board, pos, num):

    return not usedInRow(board, pos[0], num) and not usedInCol(board, pos[1], num) and not usedInBox(board, pos[0] - pos[0]%3, pos[1]-pos[1]%3)


def usedInRow(board, row, num):
    for col in range(9):
        if(board[row, col] == num):
            return True
    return False

def usedInCol(board, col,num):
    for row in range(9):
        if(board[row, col] == num):
            return True
    return False

def usedInBox(board, boxStartRow, boxStartCol, num):
    for row in range(3):
        for col in range(3):
            if(board[row+boxStartRow, col+boxStartCol] == num):
                return True
    return False

def solveSudoku(board):

    pos = [0,0]
    
    if(not findUnassignedLocation(board, pos)):
        return True

    #might need this
    #row = pos[0]
    #col = pos[1]
    
    for num in range(1,9):
        if(noConflicts(board, pos, num)):
            board[pos[0], pos[1]] = num

            if(solveSudoku(board)):
                return True
            
            board[pos[0], pos[1]] = 0
    
    return False

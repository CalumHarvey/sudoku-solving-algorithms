'''
Initial design is to have preset puzzles at different difficulties
difficulty can then be chosen and a random puzzle of that difficulty is chosen by the program
'''

import random
import os


currentDir = os.path.dirname(__file__)

def boardPicker(difficulty):
    finalBoard = []
    
    #lineNumber = random.randint(0,3)
    lineNumber = 0
    #fileName =  + str(difficulty) + ".txt"
    filePath = "puzzles/" + str(difficulty) + ".txt"
    absFilePath = os.path.join(currentDir, filePath)

    f = open(absFilePath, "r")
    allLines = f.readlines()
    line = allLines[lineNumber]

    lineStripped = line.strip()
    firstSplit = lineStripped.split(",")

    for x in firstSplit:
        splitDone = x.split(" ")
        finalBoard.append(splitDone)
    print(finalBoard)


boardPicker("easy")

    


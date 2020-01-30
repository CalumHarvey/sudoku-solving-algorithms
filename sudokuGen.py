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
    print(filePath)

    f = open(absFilePath, "r")
    allLines = f.readlines()
    line = allLines[lineNumber]

    lineStripped = line.strip()
    firstSplit = lineStripped.split(",")

    for x in firstSplit:
        splitDone = x.split(" ")
        finalBoard.append(splitDone)
    
    return finalBoard



import sudokuGen
import algorithms
import os
import numpy as np
import statistics
import random
from simanneal import Annealer
import datetime
from tkinter import *


# create dictionaries for results
timeDict = {}
passesDict = {}
algorithms = []


# Selection of algorithm - use use input from user (give each algorithm a number 1-6)
# how many algorithms to compare?
# which algorithms are going to be compared (use numbers??)
# return list of algorithms that are going to be compared
'''
def algorithmSelection():
    selectionAlgorithm = "0"
    algorithms = []

    print("Type 1 for backtracking")
    print("Type 2 for simannealing")
    print("Type 3 for Genetic")

    selectionAlgorithm = input("Select one algorithm: ")
    algorithms.append(selectionAlgorithm)

    return algorithms
'''

def difficultySelection():

    print("Select difficulty")

    #difficultySelection = input()
    difficultySelection = "1"

    return difficultySelection


class Board:
    def __init__(self):
        self.board = np.zeros((9, 9), dtype=int)
        self.numLines = 0
        cur_path = os.path.dirname(__file__)
        rel_path = "puzzles/puzzles.txt"
        self.abs_file_path = os.path.join(cur_path, rel_path)
        # on initialisation of board, pick board based on difficulty of board selected

    def getBoardfromFile(self, boardNum):

        with open(self.abs_file_path) as fp:
            lines = fp.readlines()

        return lines[boardNum]

    def formatBoard(self, stringBoard):
        arrayStrip = stringBoard.strip()
        arraySplit = arrayStrip.split(",")
        intArray = [int(i) for i in arraySplit]

        temp = [intArray[r*9:(r+1)*9] for r in range(0, 9)]

        tempBoard = np.array(temp)

        return tempBoard

    def getBoard(self, boardNumber):
        board = self.getBoardfromFile(boardNumber)
        newBoard = self.formatBoard(board)
        return newBoard

    # self: board that is being solved
    # algorithm: single algorithm that is going to be solved by the function -

    def runAlgorithm(self, algorithm):
        timeArray = []
        passesArray = []
        self.numLines = sum(1 for line in open(self.abs_file_path))

        # loop for each algorithm that wants to be run on board
        for x in range(self.numLines):
            newBoard = self.getBoard(x)

            # each algorithm file should have runAlgorithm file
            # result: a tuple of time taken and passes made by algorithm
            result = (0, 0)

            if(algorithm == "1"):
                result = algorithms.backtracking.runAlgorithm(self.board)
            elif(algorithm == "2"):
                result = algorithms.simannealing.runAlgorithm(newBoard)
            elif(algorithm == "3"):
                pass
                #result = algorithms.genetic.runAlgorithm(self.board)

            print(result[0])
            print(result[1])
            # results added to dictionary with algorithm as key and result as value
            timeArray.append(result[0])
            passesArray.append(result[1])

        return timeArray, passesArray


class Analysis:
    def __init__(self):
        self.b = Board()
        self.timeArray = []
        self.passesArray = []

    def runAllAlgorithms(self, algorithmList):
        for x in algorithmList:
            results = self.b.runAlgorithm(x)
            print("results: ", results[0], results[1])
            self.timeArray.append(results[0])
            self.passesArray.append(results[1])

    # can only test after implementing algorithms
    def timeComparison(self,algorithmList):
        for x in range(len(self.timeArray)):
            print("Time for Algorithm", algorithmList[x])
            print("Raw Data: ", self.timeArray[x])
            print("Mean: ", statistics.mean(self.timeArray[x]))

        # compare time that algorithms took to solve board to each other

    def passesComparison(self, algorithmList):
        for x in range(len(self.passesArray)):
            print("Passes for Algorithm", algorithmList[x])
            print("Raw Data: ", self.passesArray[x])
            print("Mean: ", statistics.mean(self.passesArray[x]))

        # compare number of passes to solve board to each othe


class UI:
    def __init__(self):
        self.menu = Tk()
        self.backtracking = BooleanVar()
        self.simAnneal = BooleanVar()
        self.genetic = BooleanVar()

        self.puzzleNumber = IntVar()

        self.firstRow = 80
        self.firstColumn = 50
        self.secondColumn = 250


    def userInterface(self):
        w = 500
        h = 300
        ws = self.menu.winfo_screenwidth()
        hs = self.menu.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.menu.resizable(width=False, height=False)
        frame = Frame(self.menu, height=500, width=500)
        frame.pack(side=TOP, fill=BOTH)


        algorithmsLabel = Label(self.menu, text="Algorithms", font=("Ariel", 20))
        algorithmsLabel.place(x=self.firstColumn, y=self.firstRow-20)
        sudokuGenLabel = Label(self.menu, text="Sudoku Generation", font=("Ariel", 20))
        sudokuGenLabel.place(x=self.secondColumn, y=self.firstRow-20)


        backtrackingButton = Checkbutton(frame, text="Backtracking", variable=self.backtracking, onvalue=1, offvalue=0)
        backtrackingButton.place(x=self.firstColumn, y=self.firstRow+(30*1))
        simAnnealButton = Checkbutton(frame, text="Simulated Annealing", variable=self.simAnneal, onvalue=1, offvalue=0)
        simAnnealButton.place(x=self.firstColumn, y=self.firstRow+(30*2))
        geneticButton = Checkbutton(frame, text="Genetic", variable=self.genetic, onvalue=1, offvalue=0)
        geneticButton.place(x=self.firstColumn, y=self.firstRow+(30*3))


        tenPuzzlesButton = Radiobutton(frame, text="10", variable=self.puzzleNumber, value=10)
        tenPuzzlesButton.place(x=self.secondColumn, y=self.firstRow+(30*1))
        hundredPuzzlesButton = Radiobutton(frame, text="100", variable=self.puzzleNumber, value=100)
        hundredPuzzlesButton.place(x=self.secondColumn, y=self.firstRow+(30*2))
        thousandPuzzleButton = Radiobutton(frame, text="1000", variable=self.puzzleNumber, value=1000)
        thousandPuzzleButton.place(x=self.secondColumn, y=self.firstRow+(30*3))
        self.puzzleNumber.set(10)

        genButton = Button(frame, text="Generate Boards", width=14, relief=GROOVE, command= lambda: self.generationSelection(self.puzzleNumber))
        genButton.place(x=self.secondColumn, y=self.firstRow+(30*4)+10)

        runAlgorithmButton = Button(frame, text="Run Algorithm", width=14, relief=GROOVE, command= lambda: self.algorithmSelection())
        runAlgorithmButton.place(x=self.firstColumn, y=self.firstRow+(30*4)+10)

        self.menu.mainloop()

    def generationSelection(self, puzzleNumber):
        waitingLabel = Label(self.menu, text="working...", font=("Ariel", 10))
        waitingLabel.place(x=self.secondColumn, y=self.firstRow+(30*5)+10)
        sudokuGen.runAlgorithm(int(self.puzzleNumber.get()))
        waitingLabel.config(text="done")
    
    def algorithmSelection(self):
        algorithmList = []
        if(self.backtracking.get() == True):
            algorithmList.append(1)
        if(self.simAnneal.get() == True):
            algorithmList.append(2)
        if(self.genetic.get() == True):
            algorithmList.append(3)
        
        print(self.backtracking)
        print(algorithmList)
        a = Analysis()
        a.runAllAlgorithms(algorithmList)

        self.displayAnalysis(a.timeArray, a.passesArray, algorithmList)
    
    def displayAnalysis(self, times, passes, algorithmList):
        algorithmDict = {1 : "Backtracking", 2 : "Simulated Annealing", 3 : "Genetic"}
        display = Tk()

        for x in range(len(algorithmList)):
            l1 = Label(display, text=algorithmDict.get(x+1))
            l1.grid(row=0,column=x,sticky = W, pady = 2)
            l2 = Label(display, text="Times")
            l2.grid(row=1, column=x,sticky = W, pady = 2)
            l3 = Label(display, text="Raw Data: " + str(times[x]))
            l3.grid(row=2, column=x,sticky = W, pady = 2)
            l4 = Label(display, text="Mean: " + str(statistics.mean(times[x])))
            l4.grid(row=3, column=x,sticky = W, pady = 2)

            l5 = Label(display, text="Passes")
            l5.grid(row=5, column=x,sticky = W, pady = 2)
            l6 = Label(display, text="Raw Data: " + str(passes[x]))
            l6.grid(row=6, column=x,sticky = W, pady = 2)
            l7 = Label(display, text="Mean: " + str(statistics.mean(passes[x])))
            l7.grid(row=7, column=x,sticky = W, pady = 2)
        
        display.mainloop()



            

def main():
    '''
    a = Analysis()
    a.runAllAlgorithms()
    a.timeComparison()
    a.passesComparison()
    '''
    UIinit = UI()
    UIinit.userInterface()


main()


# Generation of board - potentially use pre-existing boards for initial design and potentially write creation algorithm at the end
# Should call the board generation function in another file
# look at c++ code and also s6 project (improve s6 project version) for creating the sudoku board but create new algorithm for the numbers


# Running the selected algorithm (main)
# Can have more functions for data processing for time taken and number of passes through

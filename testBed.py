import sudokuGen
import algorithms
import os
import numpy as np
import statistics
import random
import datetime
from tkinter import *
import matplotlib.pyplot as plt
import math


# create dictionaries for results
timeDict = {}
passesDict = {}
algorithmList = []


class Board:
    def __init__(self):
        self.board = np.zeros((9, 9), dtype=int)
        self.numLines = 0
        cur_path = os.path.dirname(__file__)
        rel_path = "puzzles/puzzles.txt"
        self.abs_file_path = os.path.join(cur_path, rel_path)

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
            print(x)

            # each algorithm file should have runAlgorithm file
            # result: a tuple of time taken and passes made by algorithm
            result = (0, 0)

            if(algorithm == 1):
                result = algorithms.backtracking.runAlgorithm(newBoard)
            elif(algorithm == 2):
                result = algorithms.simannealing.runAlgorithm(newBoard)
            elif(algorithm == 3):
                pass
                result = algorithms.genetic.runAlgorithm(newBoard)
            elif(algorithm == 4):
                result = algorithms.hillClimb.runAlgorithm(newBoard)

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
            resultsTemp = []
            results = self.b.runAlgorithm(x)
            for i in results[0]:
                resultsTemp.append(float("{0:.3f}".format(i)))
            self.timeArray.append(resultsTemp)
            self.passesArray.append(results[1])



class UI:
    def __init__(self):
        self.menu = Tk()
        self.backtracking = BooleanVar()
        self.simAnneal = BooleanVar()
        self.genetic = BooleanVar()
        self.hillClimb = BooleanVar()

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
        hillClimbButton = Checkbutton(frame, text="Hill Climb", variable=self.hillClimb, onvalue=1, offvalue=0)
        hillClimbButton.place(x=self.firstColumn, y=self.firstRow+(30*2))
        simAnnealButton = Checkbutton(frame, text="Simulated Annealing", variable=self.simAnneal, onvalue=1, offvalue=0)
        simAnnealButton.place(x=self.firstColumn, y=self.firstRow+(30*3))
        geneticButton = Checkbutton(frame, text="Genetic (WIP)", variable=self.genetic, onvalue=1, offvalue=0)
        geneticButton.place(x=self.firstColumn, y=self.firstRow+(30*4))


        tenPuzzlesButton = Radiobutton(frame, text="10", variable=self.puzzleNumber, value=10)
        tenPuzzlesButton.place(x=self.secondColumn, y=self.firstRow+(30*1))
        hundredPuzzlesButton = Radiobutton(frame, text="100", variable=self.puzzleNumber, value=100)
        hundredPuzzlesButton.place(x=self.secondColumn, y=self.firstRow+(30*2))
        thousandPuzzleButton = Radiobutton(frame, text="1000", variable=self.puzzleNumber, value=1000)
        thousandPuzzleButton.place(x=self.secondColumn, y=self.firstRow+(30*3))
        tenThousandPuzzleButton = Radiobutton(frame, text="10000", variable=self.puzzleNumber, value=10000)
        tenThousandPuzzleButton.place(x=self.secondColumn, y=self.firstRow+(30*4))
        self.puzzleNumber.set(getLines())

        genButton = Button(frame, text="Generate Boards", width=14, relief=GROOVE, command= lambda: self.generationSelection(self.puzzleNumber))
        genButton.place(x=self.secondColumn, y=self.firstRow+(30*5)+10)

        runAlgorithmButton = Button(frame, text="Run Algorithm", width=14, relief=GROOVE, command= lambda: self.algorithmSelection())
        runAlgorithmButton.place(x=self.firstColumn, y=self.firstRow+(30*5)+10)

        self.menu.mainloop()

    def generationSelection(self, puzzleNumber):
        waitingLabel = Label(self.menu, text="working...", font=("Ariel", 10))
        waitingLabel.place(x=self.secondColumn, y=self.firstRow+(30*6)+10)
        sudokuGen.runAlgorithm(int(self.puzzleNumber.get()))
        waitingLabel.config(text="done")
    
    def algorithmSelection(self):
        algorithmList = []
        if(self.backtracking.get() == True):
            algorithmList.append(1)
        if(self.hillClimb.get() == True):
            algorithmList.append(4)
        if(self.simAnneal.get() == True):
            algorithmList.append(2)
        if(self.genetic.get() == True):
            algorithmList.append(3)

        
        if(len(algorithmList) == 0):

            popup = Tk()
            popup.wm_title("!")
            w = 200
            h = 80
            ws = self.menu.winfo_screenwidth()
            hs = self.menu.winfo_screenheight()
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
            popup.resizable(width=False, height=False)

            label = Label(popup, text="No algorithms selected", font=("Ariel", 10))
            label.pack(side="top", fill="x", pady=10)
            B1 = Button(popup, text="Okay", command = popup.destroy)
            B1.pack()
            popup.mainloop()
        else:
            a = Analysis()
            a.runAllAlgorithms(algorithmList)

            self.displayAnalysis(a.timeArray, a.passesArray, algorithmList)
    
    def displayAnalysis(self, times, passes, algorithmList):
        algorithmDict = {1 : "Backtracking", 2 : "Simulated Annealing", 3 : "Genetic", 4 : "Hill Climb"}
        display = Tk()
        sizex = (len(algorithmList)*400)
        sizey = 410
        posx  = 100
        posy  = 100
        display.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        fig, (ax1,ax2) = plt.subplots(2,1, figsize = (12,8))
        i = np.arange(1,self.puzzleNumber.get() + 1)

        for x in range(len(algorithmList)):
            timesAlg = times[x]
            passesAlg = passes[x]
            print(algorithmDict.get(algorithmList[x]))
            l1 = Label(display, text=algorithmDict.get(algorithmList[x]), font=("Ariel", 15))
            l1.grid(row=0,column=x,sticky = W, pady = 2)
            l2 = Label(display, text="Times", font=("Ariel", 12))
            l2.grid(row=1, column=x,sticky = W, pady = 2)
            l3 = Label(display, text="Raw Data: " + str(timesAlg[:10]))
            l3.grid(row=2, column=x,sticky = W, pady = 2)
            temp = float("{0:.2f}".format(statistics.mean(times[x])))
            l4 = Label(display, text="Mean: " + str(temp) + "s")
            l4.grid(row=3, column=x,sticky = W, pady = 2)
            temp = float("{0:.2f}".format(statistics.median(times[x])))
            l8 = Label(display, text="Median: " + str(temp) + " s")
            l8.grid(row=4, column=x,sticky = W, pady = 2)
            temp = float("{0:.2f}".format(statistics.variance(times[x])))
            l9 = Label(display, text="Variance: " + str(temp) + " s")
            l9.grid(row=5, column=x,sticky = W, pady = 2)
            temp = float("{0:.4f}".format(max(times[x])))
            l9 = Label(display, text="Max: " + str(temp) + " s")
            l9.grid(row=6, column=x,sticky = W, pady = 2)
            temp = float("{0:.4f}".format(min(times[x])))
            l9 = Label(display, text="Min: " + str(temp) + " s")
            l9.grid(row=7, column=x,sticky = W, pady = 2)


            l5 = Label(display, text="Passes", font=("Ariel", 12))
            l5.grid(row=10, column=x,sticky = W, pady = 2)
            l6 = Label(display, text="Raw Data: " + str(passesAlg[:10]))
            l6.grid(row=11, column=x,sticky = W, pady = 2)
            temp = float("{0:.2f}".format(statistics.mean(passes[x])))
            l7 = Label(display, text="Mean: " + str(temp) + " passes")
            l7.grid(row=12, column=x,sticky = W, pady = 2)
            temp = float("{0:.2f}".format(statistics.median(passes[x])))
            l8 = Label(display, text="Median: " + str(temp) + " passes")
            l8.grid(row=13, column=x,sticky = W, pady = 2)
            temp = float("{0:.2f}".format(statistics.variance(passes[x])))
            l9 = Label(display, text="Variance: " + str(temp) + " passes")
            l9.grid(row=14, column=x,sticky = W, pady = 2)
            temp = float("{0:.4f}".format(max(passes[x])))
            l9 = Label(display, text="Max: " + str(temp) + " passes")
            l9.grid(row=15, column=x,sticky = W, pady = 2)
            temp = float("{0:.4f}".format(min(passes[x])))
            l9 = Label(display, text="Min: " + str(temp) + " passes")
            l9.grid(row=16, column=x,sticky = W, pady = 2)
        
            npArrayTime = np.array(times[x])
            ax1.plot(i, npArrayTime, marker = '*', label = algorithmDict.get(algorithmList[x]))
            ax1.set_title('Times')

            npArrayPasses = np.array(passes[x])
            ax2.plot(i, npArrayPasses, marker = "*", label = algorithmDict.get(algorithmList[x]))
            ax2.set_title("Passes")
        
        plt.legend()
        plt.show()

        display.mainloop()



def getLines():
    '''Helper function for getting number of lines'''
    cur_path = os.path.dirname(__file__)
    rel_path = "puzzles/puzzles.txt"
    abs_file_path = os.path.join(cur_path, rel_path)

    return sum(1 for line in open(abs_file_path))



if __name__ == "__main__":
    
    UIinit = UI()
    UIinit.userInterface()          



# Generation of board - potentially use pre-existing boards for initial design and potentially write creation algorithm at the end
# Should call the board generation function in another file
# look at c++ code and also s6 project (improve s6 project version) for creating the sudoku board but create new algorithm for the numbers


# Running the selected algorithm (main)
# Can have more functions for data processing for time taken and number of passes through

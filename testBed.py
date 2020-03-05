import sudokuGen
import algorithms
import os
import numpy as np
import statistics

#dictionary that takes algorithm number and returns the name of the algorithm
algorithmDict = {1 : "backtracking", 2 : "genetic"}#...

#create dictionaries for results
timeDict = {}
passesDict = {}


#Selection of algorithm - use use input from user (give each algorithm a number 1-6)
#how many algorithms to compare?
#which algorithms are going to be compared (use numbers??)
#return list of algorithms that are going to be compared

def algorithmSelection():
    selectionAlgorithm = "0"
    algorithms = []

    print("Type 1 for backtracking")
    print("Type 2 for simannealing")
    print("Type 3 for Genetic")

    selectionAlgorithm = input("Select one algorithm: ")
    algorithms.append(selectionAlgorithm)

    return algorithms

def difficultySelection():

    print("Select difficulty")

    #difficultySelection = input()
    difficultySelection = "1"

    return difficultySelection


class Board:
    def __init__(self):
        self.board = np.zeros((9,9), dtype=int)
        self.numLines = 0
        cur_path = os.path.dirname(__file__)
        rel_path = "puzzles/puzzles.txt"
        self.abs_file_path = os.path.join(cur_path, rel_path)
        #on initialisation of board, pick board based on difficulty of board selected 

    def getBoardfromFile(self, boardNum):

        with open(self.abs_file_path) as fp:
            lines = fp.readlines()

        return lines[boardNum]


    def formatBoard(self, stringBoard):
        arrayStrip = stringBoard.strip()
        arraySplit = arrayStrip.split(",")
        intArray = [int(i) for i in arraySplit]

        temp = [intArray[r*9:(r+1)*9] for r in range(0,9)]

        tempBoard = np.array(temp)

        return tempBoard

        #print(temp)


        #temp = np.reshape(intArray, (9,9))
        #self.board = list(temp)

        #print(intArray)
        
        #self.board = np.reshape(intArray, (9,9))

    def getBoard(self,boardNumber):
        board = self.getBoardfromFile(boardNumber)
        newBoard = self.formatBoard(board)
        return newBoard


    
    #self: board that is being solved
    #algorithm: single algorithm that is going to be solved by the function -
    def runAlgorithm(self, algorithm):
        timeArray = []
        passesArray = []
        self.numLines = sum(1 for line in open(self.abs_file_path))

        #loop for each algorithm that wants to be run on board 
        for x in range(self.numLines):
            newBoard = self.getBoard(x)
            print("id ", id(newBoard))
            print("testBed Board: ", newBoard)

            #each algorithm file should have runAlgorithm file 
            #result: a tuple of time taken and passes made by algorithm
            result = (0 , 0)

            if(algorithm == "1"):
                result = algorithms.backtracking.runAlgorithm(self.board)
            elif(algorithm == "2"):
                result = algorithms.simannealing.runAlgorithm(newBoard)
            elif(algorithm == "3"):
                pass
                #result = algorithms.genetic.runAlgorithm(self.board)

            print(result[0])
            print(result[1])
            #results added to dictionary with algorithm as key and result as value 
            timeArray.append(result[0])
            passesArray.append(result[1])

        return timeArray, passesArray


class Analysis:
    def __init__(self):
        #self.difficulty = difficultySelection()
        self.algorithms = algorithmSelection()
        self.b = Board()
        self.timeArray = []
        self.passesArray = []

    def runAllAlgorithms(self):
        for x in self.algorithms:
            results = self.b.runAlgorithm(x)
            self.timeArray.append(results[0])
            self.passesArray.append(results[1])
    
    #can only test after implementing algorithms
    def timeComparison(self):
        for x in range(len(self.timeArray)):
            print("Time for Algorithm", self.algorithms[x])
            print("Raw Data: ", self.timeArray[x])
            print("Mean: ", statistics.mean(self.timeArray[x]))
            
        #compare time that algorithms took to solve board to each other

    def passesComparison(self):
        for x in range(len(self.passesArray)):
            print("Passes for Algorithm", self.algorithms[x])
            print("Raw Data: ", self.passesArray[x])
            print("Mean: ", statistics.mean(self.passesArray[x]))
        
        #compare number of passes to solve board to each othe


def main():
    a = Analysis()
    a.runAllAlgorithms()
    a.timeComparison()
    a.passesComparison()

main()


#Generation of board - potentially use pre-existing boards for initial design and potentially write creation algorithm at the end
#Should call the board generation function in another file
#look at c++ code and also s6 project (improve s6 project version) for creating the sudoku board but create new algorithm for the numbers


#Running the selected algorithm (main)
#Can have more functions for data processing for time taken and number of passes through

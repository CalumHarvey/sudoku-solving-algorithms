import sudokuGen

#dictionary that takes algorithm number and returns the name of the algorithm
algorithmDict = {1 : "backtracking", 2 : "genetic"}#...


#Selection of algorithm - use use input from user (give each algorithm a number 1-6)
#how many algorithms to compare?
#which algorithms are going to be compared (use numbers??)
#return list of algorithms that are going to be compared
#needs to select difficulty - dont use global variables
@staticmethod
def algorithmSelection():

    print("a description of each algorithm and how to select them all")

    selectionAlgorithm = input("Select algorithm: ")

    return selectionAlgorithm

def difficultySelection():

    print("Select difficulty")

    difficultySelection = input()

    return difficultySelection


class Board:
    def __init__(self, difficulty):
        #on initialisation of board, pick board based on difficulty of board selected 
        self.board = sudokuGen.boardPicker(difficulty)
    
    #self: board that is being solved
    #algorithm: single algorithm that is going to be solved by the function -
    def runAlgorithms(self, algorithms):

        #create dictionaries for results
        timeDict = {}
        passesDict = {}

        #loop for each algorithm that wants to be run on board 
        for x in algorithms:
            #result: a tuple of time taken and passes made by algorithm
            #each algorithm file should have runAlgorithm file 
            result = x.runAlgorithm(self.board)
            #results added to dictionary with algorithm as key and result as value 
            timeDict.update( {x : result[0]} )
            passesDict.update( {x : result[1]} )



        return timeDict, passesDict


class Analysis:
    def __init__(self):
        self.difficulty = difficultySelection()
        self.algorithms = algorithmSelection()
        self.board = Board(self.difficulty)
        self.results = self.board.runAlgorithms(self.algorithms)
    
    def timeComparison(self):
        #compare time that algorithms took to solve board to each other
        pass

    def passesComparison(self):
        #compare number of passes to solve board to each other
        pass

#Generation of board - potentially use pre-existing boards for initial design and potentially write creation algorithm at the end
#Should call the board generation function in another file
#look at c++ code and also s6 project (improve s6 project version) for creating the sudoku board but create new algorithm for the numbers


#Running the selected algorithm (main)
#Can have more functions for data processing for time taken and number of passes through




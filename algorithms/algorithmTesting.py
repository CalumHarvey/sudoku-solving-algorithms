import unittest
import numpy as np
import backtracking
import hillClimb
import simannealing
import genetic

puzzle = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])
completedPuzzle = np.array([[7, 5, 6, 1, 3, 2, 8, 9, 4],[8, 9, 2, 6, 7, 4, 5, 3, 1],[4, 3, 1, 8, 5, 9, 6, 2, 7],[5, 4, 3, 9, 6, 8, 1, 7, 2],[2, 8, 9, 3, 1, 7, 4, 5, 6],[1, 6, 7, 4, 2, 5, 3, 8, 9],[3, 7, 4, 5, 9, 6, 2, 1, 8],[9, 1, 8, 2, 4, 3, 7, 6, 5],[6, 2, 5, 7, 8, 1, 9, 4, 3]])


class TestAlgorithms(unittest.TestCase):


    '''
    Overall algorithm tests
    '''
    def test_Backtracking(self):
        tempPuzzle = np.array(backtracking.testing(puzzle))

        self.assertEqual(tempPuzzle.tolist(), completedPuzzle.tolist(), "Puzzle is solved wrong")
    
    def test_HillClimb(self):
        tempPuzzle = np.array(hillClimb.testing(puzzle))

        self.assertEqual(tempPuzzle.tolist(), completedPuzzle.tolist(), "Puzzle is solved wrong")

    def test_SimAnnealing(self):
        tempPuzzle = np.array(simannealing.testing(puzzle))

        self.assertEqual(tempPuzzle.tolist(), completedPuzzle.tolist(), "Puzzle is solved wrong")

    def test_Genetic(self):
        tempPuzzle = np.array(genetic.testing(puzzle))

        self.assertEqual(tempPuzzle.tolist(), completedPuzzle.tolist(), "Puzzle is solved wrong")


    '''
    Backtracking function tests
    '''
    def test_findUnassignedLocation(self):
        tempPuzzle = np.array([[7, 5, 6, 1, 3, 2, 8, 9, 4],[8, 9, 2, 6, 7, 4, 5, 3, 1],[4, 3, 1, 8, 5, 9, 6, 2, 7],[5, 4, 3, 9, 6, 8, 1, 7, 2],[2, 8, 9, 3, 0, 7, 4, 5, 6],[1, 6, 7, 4, 2, 5, 3, 8, 9],[3, 7, 4, 5, 9, 6, 2, 1, 8],[9, 1, 8, 2, 4, 3, 7, 6, 5],[6, 2, 5, 7, 8, 1, 9, 4, 3]])
        position = [0,0]

        b = backtracking.backtracking(tempPuzzle)
        b.findUnassignedLocation(tempPuzzle, position)

        self.assertEqual(position, [4,4], "Puzzle finds position wrong")

    def test_usedInRow(self):

        b = backtracking.backtracking(puzzle)
        self.assertTrue(b.usedInRow(puzzle, 6, 3), "not finding row duplicates")

    def test_usedInCol(self):
        b = backtracking.backtracking(puzzle)
        self.assertTrue(b.usedInCol(puzzle, 2, 1), "not finding column duplicates")
    
    def test_usedInBox(self):
        b = backtracking.backtracking(puzzle)
        self.assertTrue(b.usedInBox(puzzle, 3, 3, 7), "not finding box duplicates")


    '''
    Initialisation of puzzle testing
    '''
    def test_getBox(self):
        coords = hillClimb.getBox(3)
        expectedResult = [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]]

        self.assertEqual(coords, expectedResult, "Not returning box coordinates")


    def testInitialSolution(self):
        populatedBoard = hillClimb.initialSolution(puzzle)

        valuesCoords = hillClimb.getBox(5)

        values = [populatedBoard[i[0]][i[1]] for i in valuesCoords]

        self.assertEqual(len(values), 9, "Puzzle not intialised correctly")










if __name__ == "__main__":
    unittest.main()





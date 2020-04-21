import unittest
import numpy as np
import sudokuGen

puzzle = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])
completedPuzzle = np.array([[7, 5, 6, 1, 3, 2, 8, 9, 4],[8, 9, 2, 6, 7, 4, 5, 3, 1],[4, 3, 1, 8, 5, 9, 6, 2, 7],[5, 4, 3, 9, 6, 8, 1, 7, 2],[2, 8, 9, 3, 1, 7, 4, 5, 6],[1, 6, 7, 4, 2, 5, 3, 8, 9],[3, 7, 4, 5, 9, 6, 2, 1, 8],[9, 1, 8, 2, 4, 3, 7, 6, 5],[6, 2, 5, 7, 8, 1, 9, 4, 3]])


class TestSudokuGen(unittest.TestCase):

    def test_fillSudoku(self):
        tempPuzzle = puzzle

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

        s = sudokuGen.sudokuGen(grid)

        s.fillSudoku(grid)

        self.assertEqual(grid.count(0), 0, "Puzzle is filled wrong")

    
    def test_selectNonEmptyCell(self):
        s = sudokuGen.sudokuGen(puzzle)
        coords = s.selectEmptyCell(puzzle)

        self.assertNotEqual(puzzle[coords], 0, "cell selected is zero")


    def test_main(self):
        s = sudokuGen.sudokuGen(completedPuzzle)

        solvablePuzzle = s.main(completedPuzzle)

        self.assertEqual(solvablePuzzle.tolist().count(0), puzzle.tolist().count(0), "Puzzle created wrong")












if __name__ == "__main__":
    unittest.main()





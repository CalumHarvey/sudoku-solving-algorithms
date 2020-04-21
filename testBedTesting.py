import unittest
import numpy as np
import testBed
import os

puzzle = np.array([[7, 0, 6, 1, 3, 2, 0, 9, 0], [0, 0, 2, 6, 7, 4, 0, 3, 0], [0, 0, 1, 0, 0, 9, 0, 2, 0], [0, 4, 0, 9, 0, 0, 1, 0, 2], [2, 0, 9, 3, 0, 7, 4, 0, 6], [1, 0, 0, 0, 0, 5, 3, 8, 9], [3, 0, 0, 0, 0, 6, 2, 1, 0], [0, 1, 0, 2, 4, 3, 0, 6, 5], [6, 0, 0, 7, 0, 1, 9, 4, 0]])
completedPuzzle = np.array([[7, 5, 6, 1, 3, 2, 8, 9, 4],[8, 9, 2, 6, 7, 4, 5, 3, 1],[4, 3, 1, 8, 5, 9, 6, 2, 7],[5, 4, 3, 9, 6, 8, 1, 7, 2],[2, 8, 9, 3, 1, 7, 4, 5, 6],[1, 6, 7, 4, 2, 5, 3, 8, 9],[3, 7, 4, 5, 9, 6, 2, 1, 8],[9, 1, 8, 2, 4, 3, 7, 6, 5],[6, 2, 5, 7, 8, 1, 9, 4, 3]])


class TestTestBed(unittest.TestCase):

    def test_boardRetrieval(self):

        cur_path = os.path.dirname(__file__)
        rel_path = "puzzles/puzzles.txt"
        abs_file_path = os.path.join(cur_path, rel_path)

        with open(abs_file_path) as fp:
            lines = fp.readlines()

        arrayStrip = lines[3].strip()
        arraySplit = arrayStrip.split(",")
        intArray = [int(i) for i in arraySplit]

        temp = [intArray[r*9:(r+1)*9] for r in range(0, 9)]

        expectedResult = np.array(temp)


        b = testBed.Board()

        actualResult = b.getBoard(3)

        self.assertEqual(actualResult.tolist(), expectedResult.tolist(), "Puzzle retrieved wrong")




        









if __name__ == "__main__":
    unittest.main()





import unittest
from CrossAndCircle import *
from GameData import *
from PlayersType import *
from InputMethods import *

class TestCrossAndCircle(unittest.TestCase):

    def test_convertInputPositionToIntList(self):
        position = "b1"
        expectPosition = (1, 1)

        self.assertEqual(convertInputPositionToIntList(position), expectPosition)

    def test_checkRows(self):
        status = [['X', 'X', 'X'],[' ', ' ', ' '],[' ', ' ', ' ']]
        game = CrossAndCircle(GameDatas(3, PlayersType(1).name, status))
        expectValue = True
        self.assertEqual(game.checkRows('X'), expectValue)

    def test_checkColumns(self):
        status = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        game = CrossAndCircle(GameDatas(3, PlayersType(1).name, status))
        expectValue = True
        self.assertEqual(game.checkColumns('X'), expectValue)

    def test_checkDiagonal(self):
        status = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        game = CrossAndCircle(GameDatas(3, PlayersType(1).name, status))
        expectValue = True
        self.assertEqual(game.checkDiagonal('X'), expectValue)


if __name__ == '__main__':
    unittest.main()
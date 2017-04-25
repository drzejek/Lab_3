from unittest import TestCase
from CrossAndCircle import *
from GameData import *
from PlayersType import *

class TestCrossAndCircle(TestCase):
    def test_convertInputPositionToIntList(self):
        game = CrossAndCircle(GameDatas(3))
        position = "b1"
        expectPosition = (1, 1)

        self.assertEqual(game.convertInputPositionToIntList(position), expectPosition)

    def test_checkRows(self):
        status = [['X', 'X', 'X'],[' ', ' ', ' '],[' ', ' ', ' ']]
        game = CrossAndCircle(GameDatas(3, PlayersType.PlayersToPlayers, status))
        expectValue = True
        self.assertEqual(game.checkRows('X'), expectValue)

    def test_checkColumns(self):
        status = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        game = CrossAndCircle(GameDatas(3, PlayersType.PlayersToPlayers, status))
        expectValue = True
        self.assertEqual(game.checkColumns('X'), expectValue)

    def test_checkDiagonal(self):
        status = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        game = CrossAndCircle(GameDatas(3, PlayersType.PlayersToPlayers, status))
        expectValue = True
        self.assertEqual(game.checkDiagonal('X'), expectValue)


if __name__ == '__main__':
    test = TestCrossAndCircle()
    test.test_convertInputPositionToIntList()
    #test.test_checkRows()
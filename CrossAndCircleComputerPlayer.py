from CrossAndCircle import *
from InputMethods import inputPosition
import random
import sys

class CrossAndCircleComputerPlayer (CrossAndCircle):
    def move(self, charac):
        if charac == 'X':
            self.moveX()
        else:
            self.moveO()


    def doIQuitGame(self, end):
        if (end == "q"):
            print("Goodbye!")
            sys.exit()

    def moveX(self):
        self.newInputPosition = []

        while True:
            position = inputPosition(self.level, 'X')
            self.doIQuitGame(position)
            if not self.isPositionOccupied(position):
                break
        self.list2DState[self.newInputPosition[1]][self.newInputPosition[0]] = 'X'
        self.listPositionsOccupied.append(self.newInputPosition)
        self.printBoard()
        self.doEndGame('X')

    def moveO(self):
        self.newRandPosition = []

        self.getRandomPositionAndCheckIsOccupied()
        self.list2DState[self.newRandPosition[1]][self.newRandPosition[0]] = 'O'
        self.listPositionsOccupied.append(self.newRandPosition)
        self.printBoard()
        self.doEndGame('O')

    def randPosition(self):
        positionX = random.randint(0, self.level-1)
        positionY = random.randint(0, self.level-1)

        return positionX, positionY

    def getRandomPositionAndCheckIsOccupied(self):
        print("Player 'O': Computer position", end=": ")

        while True:
            self.newRandPosition = self.randPosition()
            if self.newRandPosition in self.listPositionsOccupied:
                print("This position is engaged, Try again:", end=" ")
            else:
                break

    def doNobodyWin(self):
        listLength = len(self.listPositionsOccupied)
        endLength = self.level * self.level
        if listLength == endLength:
            print("Sorry, nobody win this game :(")
            sys.exit()

    def endGame(self, charach):
        end = "End of the game. Player '" + charach + "' won"
        self.msgEnd = end
        print(self.msgEnd)
        sys.exit()

    def doEndGame(self, charach):
        if self.checkBoard(charach):
            self.endGame(charach)

        self.doNobodyWin()
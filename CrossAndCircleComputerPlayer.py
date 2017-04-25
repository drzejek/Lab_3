from CrossAndCircle import *
import random

class CrossAndCircleComputerPlayer (CrossAndCircle):
    def move(self, charac):
        if charac == 'X':
            self.moveX()
        else:
            self.moveO()

    def moveX(self):
        self.newInputPosition = []
        print("Player 'X': Input your position", end=": ")

        self.getInputPositionAndCheckIsOccupied()
        self.list2DState[self.newInputPosition[1]][self.newInputPosition[0]] = 'X'
        self.listPositionsOccupied.append(self.newInputPosition)
        PrintBoard(self.list2DState)
        self.doEndGame('X')

    def moveO(self):
        self.newRandPosition = []
        print("Player 'O': Computer position", end=": ")

        self.getRandomPositionAndCheckIsOccupied()
        self.list2DState[self.newRandPosition[1]][self.newRandPosition[0]] = 'O'
        self.listPositionsOccupied.append(self.newRandPosition)
        PrintBoard(self.list2DState)
        self.doEndGame('O')

    def randPosition(self):
        positionX = random.randint(0, self.level-1)
        positionY = random.randint(0, self.level-1)

        return positionX, positionY

    def getRandomPositionAndCheckIsOccupied(self):
        while True:
            self.newRandPosition = self.randPosition()
            print(self.newRandPosition)
            print(self.getList2DState())
            print(chr(self.newRandPosition[0]+97) + "" + str(self.newRandPosition[1]))
            if self.newRandPosition in self.listPositionsOccupied:
                print("This position is engaged, Try again:", end=" ")
            else:
                break

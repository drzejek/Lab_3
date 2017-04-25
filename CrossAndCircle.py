#!/usr/bin/env python3.4

from PrintBorad import PrintBoard
from Exceptions import *
import string
import sys

class CrossAndCircle:
    def __init__(self, gameDatas):
        self.level = gameDatas.getLevel()
        self.endNumber = 3
        self.boardSize = gameDatas.getLevel()
        self.list2DState = gameDatas.getStates()
        self.listPositionsOccupied = []
        self.setListPositionsOccupied()
        self.countNumber = 0
        PrintBoard(self.list2DState)

    #GETTERS
    def getLevel(self):
        return self.level

    def getList2DState(self):
        return self.list2DState

    def getListPositionsOccupied(self):
        return self.listPositionsOccupied

    # SETTERS
    def setListPositionsOccupied(self):
        for xPos in range(self.level):
            for yPos in range(self.level):
                if self.list2DState[xPos][yPos] != ' ':
                    self.listPositionsOccupied.append((yPos, xPos))
        print(self.listPositionsOccupied)

    #INPUT CHECKERS
    def doQuitGame(self, position):
        if position == 'q':
            print("Goodbye!")
            sys.exit()

    def isInputLengthCorrect(self, position):
        if len(position) != 2:
            raise WrongStringLength

    def isInputSyntaxCorrect(self, position):
        if not position[0] in string.ascii_lowercase:
            raise NotString

    def convertInputPositionToIntList (self, position):
        positionX, positionY = position
        positionX = ord(positionX) - 97
        positionY = int(positionY)
        return positionX, positionY

    #INPUT POSITION
    def getInputPosition(self):
        while True:
            try:
                position = input()
                self.doQuitGame(position)
                self.isInputLengthCorrect(position)
                self.isInputSyntaxCorrect(position)
                positionX, positionY = self.convertInputPositionToIntList(position)

                if 0 <= positionX < self.level and 0 <= positionY < self.level:
                    return positionX, positionY
                else:
                    raise WrongPositionInput

            except NotString:
                print("Sorry, first character is not string. Try again:", end=" ")
            except WrongPositionInput:
                print("Sorry, You type wrong position:", end=" ")
                continue
            except WrongStringLength:
                print("Sorry, Your String has wrong length. Try again:", end=" ")

    #CHECKERS
    def checkBoard(self, charach):
        if self.checkColumns(charach) or self.checkRows(charach) or self.checkDiagonal(charach): return True
        else: return False

    def checkRows(self, charac):
        for i in range(self.level):
            self.countNumber = 0
            for j in range(self.level):
                if self.isElementEqualChar(self.list2DState[i][j],charac):
                    return True
        return False

    def checkColumns(self, charac):
        for j in range(self.level):
            self.countNumber = 0
            for i in range(self.level):
                if self.isElementEqualChar(self.list2DState[i][j],charac):
                    return True
        return False

    def checkDiagonal(self, charac):
        self.countNumber = 0
        for i in range(self.level):
            if self.isElementEqualChar(self.list2DState[i][i],charac):
                return True

        self.countNumber = 0
        for i in range(self.level):
            if self.isElementEqualChar(self.list2DState[i][self.level-(i+1)],charac):
                return True
        return False

    def isElementEqualChar(self, elem, charac):
        if elem == charac:
            self.countNumber += 1
            if self.countNumber == self.endNumber:
                return True

        return False

    def doNobodyWin(self):
        listLength = len(self.listPositionsOccupied)
        endLength = self.level*self.level
        if listLength == endLength:
            print("Sorry, nobody win this game :(")
            sys.exit()
        return False

    def endGame(self,charach):
        print("End of the game. Player '" + charach + "' won")
        sys.exit()

    def doEndGame(self, charach):
        if self.checkBoard(charach):
            self.endGame(charach)

        self.doNobodyWin()

    def getInputPositionAndCheckIsOccupied(self):
        while True:
            self.newInputPosition = self.getInputPosition()
            if self.newInputPosition in self.listPositionsOccupied:
                print("This position is engaged, Try again:", end=" ")
            else:
                break

    def move(self, charac):
        pass
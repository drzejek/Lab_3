#!/usr/bin/env python3.4

from getPosition import getPosition
from PrintBorad import PrintBoard

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

    def getLevel(self):
        return self.level

    def getList2DState(self):
        return self.list2DState

    def getListPositionsOccupied(self):
        return self.listPositionsOccupied

    def setListPositionsOccupied(self):
        for xPos in range(self.level):
            for yPos in range(self.level):
                if self.list2DState[xPos][yPos] != ' ':
                    self.listPositionsOccupied.append((yPos, xPos))
        print(self.listPositionsOccupied)

    def checkRows(self, charac):
        for i in range(self.level):
            self.countNumber = 0
            for j in range(self.level):
                if self.isElementEqualChar(self.list2DState[i][j],charac):
                    return True

    def checkColumns(self, charac):
        for j in range(self.level):
            self.countNumber = 0
            for i in range(self.level):
                if self.isElementEqualChar(self.list2DState[i][j],charac):
                    return True

    def checkDiagonal(self, charac):
        self.countNumber = 0
        for i in range(self.level):
            if self.isElementEqualChar(self.list2DState[i][i],charac):
                return True

        self.countNumber = 0
        for i in range(self.level):
            if self.isElementEqualChar(self.list2DState[i][self.level-(i+1)],charac):
                return True

    def isElementEqualChar(self, elem, charac):
        if elem == charac:
            self.countNumber += 1
            if self.countNumber == self.endNumber:
                return True

    def doNobodyWin(self):
        listLength = len(self.listPositionsOccupied)
        endLength = self.level*self.level
        if listLength == endLength:
            print("Sorry, nobody won this game :(")
            sys.exit() 
 
    def doEndGame(self, charach):

        if self.checkColumns(charach):
            return True
        if self.checkRows(charach):
            return True
        if self.checkDiagonal(charach):
            return True
        else:
            return False

    def move(self, charac):
        print("Player '" + charac + "': Input your position", end=": ")
        position = getPosition(self.getLevel())
        
        while True:
            if position in self.listPositionsOccupied:
                print("This position is engaged, Try again:", end=" ")
                position = getPosition(self.level)
            else:
                break

        self.list2DState[position[1]][position[0]] = charac
        self.listPositionsOccupied.append(position)
        PrintBoard(self.list2DState)
        self.doNobodyWin()
        
        if self.doEndGame(charac):
            print("End of the game. Player 'X' won")
            sys.exit() 



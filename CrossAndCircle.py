#!/usr/bin/env python3.4

from PrintBorad import PrintBoard

class CrossAndCircle:
    def __init__(self, gameDatas):
        self.level = gameDatas.getLevel()
        self.endNumber = 3
        self.boardSize = gameDatas.getLevel()
        self.list2DState = gameDatas.getStates()
        self.listPositionsOccupied = []
        self.setListPositionsOccupied()
        self.countNumber = 0
        self.board = PrintBoard(self.list2DState)
        self.strBoard = self.board.getStringBoard(self.list2DState)
        self.strMsg = str(self.level)


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

    def isPositionOccupied(self, position):
        self.newInputPosition = position

        if self.newInputPosition in self.listPositionsOccupied:
            print("This position is engaged, Try again\n")
            return True
        else:
            return False

    def addCharacterAndPositionToLists(self, charac):
        self.list2DState[self.newInputPosition[1]][self.newInputPosition[0]] = charac
        self.listPositionsOccupied.append(self.newInputPosition)

    def printBoard(self):
        self.strBoard = self.board.getStringBoard(self.list2DState)
        print("\n" + self.strBoard)

    def convertStrToTuple(self, str):
        return int(str[1]), int(str[4])

    def move(self, charac):
        pass

    def infoMessage(self):
        print("Please type your position (a-" + chr(ord('a') + self.level - 1) + ")(0-"
              + str(self.level - 1) + "). For example a2, b1")
        print("To end game press 'q'")
        print("Game is being saved automaticly, every 2 moves (Cross and Circle)")

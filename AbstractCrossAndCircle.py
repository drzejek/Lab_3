from abc import ABCMeta, abstractmethod

class AbstracCrossAndCircle:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getLevel(self):
        pass

    @abstractmethod
    def getList2DState(self):
        pass

    @abstractmethod
    def getListPositionsOccupied(self):
        pass

    @abstractmethod
    # SETTERS
    def setListPositionsOccupied(self):
        pass

    @abstractmethod
    # CHECKERS
    def checkBoard(self, charach):
        pass

    @abstractmethod
    def checkRows(self, charac):
        pass

    @abstractmethod
    def checkColumns(self, charac):
        pass

    @abstractmethod
    def checkDiagonal(self, charac):
        pass

    @abstractmethod
    def isElementEqualChar(self, elem, charac):
        pass

    @abstractmethod
    def isPositionOccupied(self, position):
        pass

    @abstractmethod
    def addCharacterAndPositionToLists(self, charac):
        pass

    @abstractmethod
    def printBoard(self):
        pass

    @abstractmethod
    def convertStrToTuple(self, str):
        pass

    @abstractmethod
    def move(self, charac):
        pass

    @abstractmethod
    def infoMessage(self):
        pass

    @abstractmethod
    def doIQuitGame(self, msg):
        pass

    @abstractmethod
    def moveX(self):
        pass

    @abstractmethod
    def moveO(self):
        pass

    @abstractmethod
    def randPosition(self):
        pass

    @abstractmethod
    def getRandomPositionAndCheckIsOccupied(self):
        pass

    @abstractmethod
    def doNobodyWin(self):
        pass

    @abstractmethod
    def endGame(self, charach):
        pass

    @abstractmethod
    def doEndGame(self, charach):
        pass
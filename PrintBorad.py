#!/usr/bin/env python3.4

class PrintBoard:

    @classmethod
    def __init__(self, listCrossAndCircle):
        self.listCrossAndCircle = listCrossAndCircle
        self.rows = len(listCrossAndCircle)

        pass


    def getStringBoard(self, listCrossAndCircle):
        stringBoard = self.printXPosition()

        position = 0
        yPosition = 0
        for x in self.listCrossAndCircle:
            stringBoard += str(yPosition)
            yPosition +=1
            for element in x:
                position += 1
                stringBoard += " " + str(element) + " "
                if self.doBreakLine(position):
                    stringBoard += self.printHorizontalSeparator(position)
                else:
                    stringBoard += self.printVerticalSeparator()
        stringBoard += "\n"
        return stringBoard

    def printHorizontalSeparator(self, position):
        strHorizon = ""
        if position%self.rows==0:
            strHorizon += "\n"
            strHorizon += " "
            for ix in range(self.rows):
                strHorizon += "--- "
            strHorizon += "\n"
        else:
            strHorizon += "\n"
        return strHorizon

    def printVerticalSeparator(self):
        return "|"

    def doBreakLine(self, position):
        if position%self.rows==0:
            return True
        else:
            return False

    def printXPosition(self):
        strXPos = " "
        for number in range(self.rows):
            strXPos += ' ' + chr(ord('a') + number) + '  '
        strXPos += "\n"
        return strXPos
#!/usr/bin/env python3.4

from math import *

class PrintBoard:

    @classmethod
    def __init__(self, listCrossAndCircle):
        self.listCrossAndCircle = listCrossAndCircle
        self.rows = len(listCrossAndCircle)

        self.printXPosition()

        position = 0
        yPosition = 0
        for x in listCrossAndCircle:
            print(yPosition, end='')
            yPosition +=1
            for element in x:
                position += 1
                print(' ' + element + ' ', end='')
                if PrintBoard.doBreakLine(position):
                    PrintBoard.printHorizontalSeparator(position)
                else:
                    PrintBoard.printVerticalSeparator()
        print()

    @classmethod
    def printHorizontalSeparator(self, position):
        if position%self.rows==0:
            print()
            print(' ', end='')
            [print('--- ', end='') for ix in range(self.rows)]
            print()
        else:
            print()

    @classmethod
    def printVerticalSeparator(self):
        print('|', end='')

    @classmethod
    def doBreakLine(self, position):
        if position%self.rows==0:
            return True
        else:
            return False

    @classmethod
    def printXPosition(self):
        print(' ', end='')
        for number in range(self.rows):
            print(' ' + chr(ord('a') + number) + ' ', end=' ')
        print()

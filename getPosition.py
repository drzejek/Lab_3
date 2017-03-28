#!/usr/bin/env python3.4

from Exceptions import *
import string
import sys

def getPosition(level):
    while True:
        try:
            position = input()

            if position == 'q':
                print("Do zobaczenia!")
                sys.exit()

            if len(position) != 2:
                raise WrongStringLength

            positionX, positionY = position

            if not positionX in string.ascii_lowercase:
                raise NotString

            positionX = ord(positionX) - 97
            positionY = int(positionY)

            if 0 <= positionX < level and 0 <= positionY < level:
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


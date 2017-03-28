#!/usr/bin/env python3.4
import sys

from getPosition import getPosition
from CrossAndCircle import CrossAndCircle
from InputAndOutput import *


   
def main():
    datas = InputAndOutput.inputDatas()
    gameCrossAndCicle = CrossAndCircle(datas)

    print("Please type your position (a-" + chr(ord('a') + gameCrossAndCicle.getLevel() - 1) + ")(0-"
          + str(gameCrossAndCicle.getLevel() - 1) + "). For example a2, b1")

    while True:
        gameCrossAndCicle.move('X')
        gameCrossAndCicle.move('O')
 
        InputAndOutput.saveToFileGameDatas(datas, gameCrossAndCicle.getList2DState())

if __name__ == '__main__':
    main()



#!/usr/bin/env python3.4

from CrossAndCirclePlayerPlayer import *
from CrossAndCircleComputerPlayer import *
from InputAndOutputMethods import *
   
def main():
    datas = inputDatas()
    if datas.getPlayers() == PlayersType.PlayersToPlayers:
        gameCrossAndCicle = CrossAndCirclePlayerPlayer(datas)
    else:
        gameCrossAndCicle = CrossAndCircleComputerPlayer(datas)

    print("Please type your position (a-" + chr(ord('a') + gameCrossAndCicle.getLevel() - 1) + ")(0-"
          + str(gameCrossAndCicle.getLevel() - 1) + "). For example a2, b1")

    while True:
        gameCrossAndCicle.move('X')
        gameCrossAndCicle.move('O')
 
        saveToFileGameDatas(datas, gameCrossAndCicle.getList2DState())
        print("Game datas has been saved")
if __name__ == '__main__':
    main()



#!/usr/bin/env python3.4

from CrossAndCircleComputerPlayer import *
from CrossAndCirclePlayerServer import *
from InputMethods import *
from OutputMethods import *
from PlayersType import *

def main():
    datas = inputDatas()
    if datas.getPlayers() == 'PlayerToPlayer':
        gameCrossAndCicle = CrossAndCirclePlayerServer(datas)
    else:
        gameCrossAndCicle = CrossAndCircleComputerPlayer(datas)

    gameCrossAndCicle.infoMessage()
    gameCrossAndCicle.printBoard()
    while True:
        gameCrossAndCicle.move('X')
        gameCrossAndCicle.move('O')

        saveToFileGameDatas(datas, gameCrossAndCicle.getList2DState())
if __name__ == '__main__':
    main()



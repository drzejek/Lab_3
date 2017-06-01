from GameData import GameDatas
from PlayersType import *
import os
from pathlib import Path

def saveToFileGameDatas(gameData, listOfState):
    with open(os.path.dirname(__file__)+'\cross_and_circle.dat', 'w') as fp:
        fp.write(str(gameData.getLevel()) + "\n")
        fp.write(str(gameData.getPlayers()) + "\n")
        fp.writelines('_'.join(str(j) for j in i) + '\n' for i in listOfState)

    print("Game datas has been saved")

def loadFromFileGameDatas():
    my_file = Path(os.path.dirname(__file__)+'\cross_and_circle.dat')
    print(my_file.exists()  )
    if my_file.exists():
        with open(os.path.dirname(__file__) + '\cross_and_circle.dat', 'r') as fp:
            level = int(fp.readline())
            player = fp.readline()
            player = player[:-1]
            player = PlayersType[player].name
            print(player)
            listOfState = []
            for line in fp.readlines():
                listOfState.append(line.strip('\n').split('_'))

            return GameDatas(level, player, listOfState)
    else:
        print("No file, where data of game hav been saved")
        return False




from GameData import GameDatas
from Exceptions import *
from PlayersType import *

def inputNewGameDatas():
    level = inputGameLevel()
    players = inputGamePlayers()
    list = None

    return GameDatas(level, players, list)

def inputGameLevel():
    print("Please enter a level (numbers 3-10):", end=" ")
    while True:
        try:
            level = int(input())
            if not 2 < level < 11:
                raise NumberOutOfBounds
            return level
        except NumberOutOfBounds:
            print("Sorry, wrong number. Try again: ", end=" ")
            continue

def inputGamePlayers():
    print("Please choose palyers: Players vs. Player (p) or Players vs. Computer (c):", end=" ")
    while True:
        try:
            players = input()

            if players == 'p':
                playersType = PlayersType.PlayersToPlayers
            elif players == 'c':
                playersType = PlayersType.PlayersToComputer
            else:
                raise WrongCharacter

            return playersType

        except WrongCharacter:
            print("Sorry, wrong number. Try again", end=" ")
            continue

def saveToFileGameDatas(gameData, listOfState):
    with open('cross_and_circle.dat', 'w') as fp:
        fp.write(str(gameData.getLevel()) + "\n")
        fp.write(str(gameData.getPlayers().value) + "\n")
        fp.writelines('_'.join(str(j) for j in i) + '\n' for i in listOfState)

def loadFromFileGameDatas():
    with open('cross_and_circle.dat', 'r') as fp:
        level = int(fp.readline())
        player = int(fp.readline())
        listOfState = []
        for line in fp.readlines():
            listOfState.append(line.strip('\n').split('_'))

        return GameDatas(level, player, listOfState)

def inputDatas():
    print("Do you want new game (n) or load previous game (l)?:", end=" ")
    while True:
        try:
            game = input()

            if game == 'n':
                return inputNewGameDatas()
            elif game == 'l':
                return loadFromFileGameDatas()
            else:
                raise WrongCharacter

        except WrongCharacter:
            print("Sorry, I didn't understand that. Try again:", end=" ")
            continue

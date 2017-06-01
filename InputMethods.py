from InputCheckers import *
from OutputMethods import *

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
                playersType = PlayersType(1).name
            elif players == 'c':
                playersType = PlayersType(2).name
            else:
                raise WrongCharacter

            return playersType

        except WrongCharacter:
            print("Sorry, wrong number. Try again", end=" ")
            continue

def inputPosition(level, charac):
    while True:
        try:
            print("Player '" + charac + "': Input your position", end=": ")
            position = input()
            if position == 'q':
                return position
            #doQuitGame(position)
            isInputLengthCorrect(position)
            isInputSyntaxCorrect(position)
            positionX, positionY = convertInputPositionToIntList(position)

            if 0 <= positionX < level and 0 <= positionY < level:
                return positionX, positionY
            else:
                raise WrongPositionInput

        except NotString:
            print("Sorry, first character is not string. Try again:", end="\n")
        except WrongPositionInput:
            print("Sorry, You type wrong position. Try again:", end="\n")
            continue
        except WrongStringLength:
            print("Sorry, Your String has wrong length. Try again:", end="\n")

def inputDatas():
    while True:
        try:
            print("Do you want new game (n) or load previous game (l)?:", end=" ")
            game = input()

            if game == 'n':
                return inputNewGameDatas()
            elif game == 'l':
                data = loadFromFileGameDatas()
                if data:
                    return data
                else:
                    continue
            else:
                raise WrongCharacter

        except WrongCharacter:
            print("Sorry, I didn't understand that. Try again")
            continue

def decodeString(str):
    return str.decode('utf8')

def encodeString(str):
    return str.encode()

def strToBool(str):
    if str == 'True':
        return True
    elif str == 'False':
        return False
    else:
        raise ValueError

def convertInputPositionToIntList(position):
    positionX, positionY = position
    positionX = ord(positionX) - 97
    positionY = int(positionY)
    return positionX, positionY

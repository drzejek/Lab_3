from CrossAndCircle import *
from InputMethods import *
import socket
import sys

class CrossAndCirclePlayerServer(CrossAndCircle):
    def __init__(self, gameDatas):
        CrossAndCircle.__init__(self, gameDatas)
        self.addres = 'localhost'
        self.port = 50001
        self.data_size = 1024
        self._createTcpIpSocket()
        self.server_address = (self.addres, self.port)
        self._bindToServer()
        self.handle_connection()

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _bindToServer(self):
        self.sock.bind(self.server_address)

    def handle_connection(self):
        self.sock.listen(1)
        print("Waiting to client...")
        self.connection, self.client_address = self.sock.accept()
        self.sendWelcomeMsg()

    def sendWelcomeMsg(self):
        self.connection.send(("Hello\n\n" + self.strBoard).encode())
        #sending client level of the game
        self.connection.send(str(self.level).encode())

    def sendDoEndGame(self, charac):
        if self.doEndGame(charac):
            self.connection.send(encodeString(charac))
            sys.exit()
        else:
            self.connection.send(encodeString(" "))

    def doIQuitGame(self, end):
        if (end == "q"):
            print("Goodbye!")
            self.connection.send(encodeString("Quit"))
            sys.exit()


    def doEnemyQuitGame(self, end):
        end = decodeString(end)
        if (end == "Quit"):
            print("Your enemy quit the game")
            sys.exit()

    def move(self, charac):
        self.newInputPosition = []

        while True:
            if(charac == 'X'):
                position = inputPosition(self.level, charac)
                self.doIQuitGame(position)
                if not self.isPositionOccupied(position):
                    break
            else:
                print("Waiting for enemy move")
                data = self.connection.recv(self.data_size)
                self.doEnemyQuitGame(data)
                move = decodeString(data)
                position = self.convertStrToTuple(move)
                isOccup = self.isPositionOccupied(position)
                if isOccup:
                    self.connection.send(encodeString(str(True)))
                else:
                    self.connection.send(encodeString(str(False)))
                    break

        self.addCharacterAndPositionToLists(charac)
        self.printBoard()
        self.connection.send(encodeString("\n"+self.strBoard))
        self.sendDoEndGame(charac)

    def doNobodyWin(self):
        listLength = len(self.listPositionsOccupied)
        endLength = self.level * self.level
        if listLength == endLength:
            print("Sorry, nobody win this game :(")
            return True
        return False

    def endGame(self, charach):
        end = "End of the game. Player '" + charach + "' won"
        self.msgEnd = end
        print(self.msgEnd)
        return True

    def doEndGame(self, charach):
        if self.checkBoard(charach):
            return self.endGame(charach)

        return self.doNobodyWin()

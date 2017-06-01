import socket
from InputMethods import *
import sys

class MyEchoClient:
    def __init__(self, addres, port, data_size):
        self.address = addres
        self.port = port
        self.data_size = data_size
        self._createTcpIpSocket()
        self._connectToServer(addres, port)
        self.level = 0

    def getWelcomeMsg(self):
        welcome = self.sock.recv(self.data_size)
        print(decodeString(welcome))

    def getLevel(self):
        lvl = self.sock.recv(self.data_size)
        self.level = int(decodeString(lvl))

    def doIQuitGame(self, end):
        if (end == "q"):
            print("Goodbye!")
            self.sock.send(encodeString("Quit"))
            sys.exit()

    def doEnemyQuitGame(self, end):
        end = decodeString(end)
        if (end == "Quit"):
            print("Your enemy quit the game")
            sys.exit()

    def isEndGame(self):
        charac = self.sock.recv(self.data_size)
        charac = decodeString(charac)
        if charac == "X" or charac == "O":
            print("End of the game. Player '" + charac + "' won")
            return True
        else:
            return False

    def getEnemyMove(self):
        print("Waiting for move")
        msg = self.sock.recv(self.data_size)
        self.doEnemyQuitGame(msg)
        print(decodeString(msg))

    def infoMessage(self):
        print("Please type your position (a-" + chr(ord('a') + self.level - 1) + ")(0-"
              + str(self.level - 1) + "). For example a2, b1")

    def sendMyMove(self):

        while True:
            inputPos = inputPosition(self.level ,'O')
            self.doIQuitGame(inputPos)
            self.sock.send(encodeString(str(inputPos)))
            isOccup = strToBool(decodeString(self.sock.recv(self.data_size)))

            if isOccup:
                print("This position is engaged, Try again\n")
                continue
            else:
                board = self.sock.recv(self.data_size)
                print(decodeString(board))
                break

    def _createTcpIpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connectToServer(self, addres, port):
        server_address = (addres, port)
        self.sock.connect(server_address)

if __name__ == "__main__":
    server = MyEchoClient('localhost', 50001, 1024)
    server.getWelcomeMsg()
    server.getLevel()
    server.infoMessage()
    while True:
        server.getEnemyMove()
        if server.isEndGame():  break
        server.sendMyMove()
        if server.isEndGame():  break

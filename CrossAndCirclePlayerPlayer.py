from CrossAndCircle import *

class CrossAndCirclePlayerPlayer (CrossAndCircle):
    def move(self, charac):
        self.newInputPosition = []
        print("Player '" + charac + "': Input your position", end=": ")

        self.getInputPositionAndCheckIsOccupied()
        self.list2DState[self.newInputPosition[1]][self.newInputPosition[0]] = charac
        self.listPositionsOccupied.append(self.newInputPosition)
        PrintBoard(self.list2DState)
        self.doEndGame(charac)
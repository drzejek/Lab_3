#!/usr/bin/env python3.4

class GameDatas:
    def __init__(self, level, players=0, states = None):
        self.level = level
        self.players = players
        self.states = []
        self.occupied = []

        if states is None:
            for row in range(level): self.states += [[' '] * level]
        else:
            self.states = states

    def getLevel(self):
        return self.level

    def getPlayers(self):
        return self.players

    def getStates(self):
        return self.states
from .player import Player


class LocalPlayer(Player):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

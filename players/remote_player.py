from interactions.console import Console
from .player import Player
from networking.server import Server
from networking.client import Client


class RemotePlayer(Player):
    def __init__(self, connected_device):
        self._connected_device = connected_device

    def choose_piece(self, piece_values):
        pass

    def place_piece(self, piece):
        pass

    def __str__(self):
        return "ZDALNY"
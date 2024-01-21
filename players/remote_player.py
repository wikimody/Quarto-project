from .player import Player


class RemotePlayer(Player):
    def __init__(self, connected_device):
        self._connected_device = connected_device

    def choose_piece(self, piece_values):
        pass

    def where_place_piece(self, piece):
        pass

    def __str__(self):
        return "ZDALNY"

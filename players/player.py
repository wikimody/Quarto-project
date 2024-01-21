from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def choose_piece(self, pieces_values):
        pass

    @abstractmethod
    def where_place_piece(self, piece=None, board=None):
        pass

    @abstractmethod
    def __str__(self):
        pass

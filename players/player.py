from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def choose_piece(self, pieces):
        pass

    @abstractmethod
    def place_piece(self, piece):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

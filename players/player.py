from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def __str__(self):
        pass

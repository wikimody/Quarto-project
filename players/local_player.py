from interactions.console import Console
from .player import Player


class LocalPlayer(Player):
    def __init__(self, name):
        self._name = name

    def choose_piece(self, piece_values):
        return Console.input_number("Wybierz figurę dla przeciwnika: ", piece_values)

    def where_place_piece(self, piece=None, board=None):
        row = Console.input_number_in_range("Wybierz rząd (1-4): ", 1, 4)
        col = Console.input_number_in_range("Wybierz kolumnę (1-4): ", 1, 4)
        while board is not None and not board.is_avaliable(row, col):
            Console.output("Pole jest już zajęte! Wybierz inne.")
            row = Console.input_number_in_range("Wybierz rząd (1-4): ", 1, 4)
            col = Console.input_number_in_range("Wybierz kolumnę (1-4): ", 1, 4)
        return row, col

    def __str__(self):
        return self._name

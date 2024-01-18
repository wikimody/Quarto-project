import random

from interactions.debug_console import Console
from .piece import Piece

from cpp_bots.cpp_adapter import CppAdapter

class QuartoGame:
    def __init__(self, board, player1, player2):
        self._board = board
        self._players = [player1, player2]
        self._turn = random.randint(0, 1)
        self._avaliable_pieces = [Piece(val) for val in range(16)]

    def next_turn(self):
        self._turn = (self._turn + 1) % 2

    def current_player(self):
        return self._players[self._turn]

    def other_player(self):
        return self._players[(self._turn + 1) % 2]

    # looks for a piece with given value and returns it (returns None if not found)
    def find_piece(self, piece_value):
        for piece in self._avaliable_pieces:
            if piece.decimal() == piece_value:
                return piece
        return None

    def avaliable_piece_values(self):
        return [piece.decimal() for piece in self._avaliable_pieces]

    # returns list of pieces in readable format (string)
    def format_avaliable_pieces(self):
        readable_pieces = "|"
        for piece in self._avaliable_pieces:
            piece_value = piece.decimal()
            # column spacing adjusting
            if piece_value < 10:
                readable_pieces += f"  {piece_value}  |"
            else:
                readable_pieces += f"  {piece_value} |"
        readable_pieces += "\n"
        readable_pieces += "|-----" * len(self._avaliable_pieces) + "|\n"

        readable_pieces += "|"
        for piece in self._avaliable_pieces:
            readable_pieces += f" {piece.symbolic()[0]} {piece.symbolic()[1]} |"
        readable_pieces += "\n"

        readable_pieces += "|"
        for piece in self._avaliable_pieces:
            readable_pieces += f" {piece.symbolic()[2]} {piece.symbolic()[3]} |"
        readable_pieces += "\n"

        return readable_pieces

    def display_preturn_state(self):
        Console.output(self._board)
        Console.output("Kolej gracza %s" % self.current_player())
        Console.output("Dostępne figury: \n%s" % self.format_avaliable_pieces())

    def display_postturn_state(self):
        Console.output(self._board)
        Console.output("Gracz %s stawia figurę." % self.other_player())

    def start(self):
        # Game is going on while there are pieces to choose from
        while len(self._avaliable_pieces):
            current_player = self.current_player()  # player that picks a piece
            other_player = self.other_player()  # player that places it down

            self.display_preturn_state()

            # current player chooses piece for the opponent
            piece_value = current_player.choose_piece(self.avaliable_piece_values())
            piece = self.find_piece(piece_value)
            self._avaliable_pieces.remove(piece)

            Console.clear_view()
            self.display_postturn_state()

            Console.output("Otrzymana figura: \n%s" % piece)
            while True:  # loops until piece is correctly placed on board
                row, col = other_player.place_piece(piece)

                if self._board.is_avaliable(row, col):  # True if piece can be correctly placed
                    self._board.place(piece, row, col)
                    if self._board.is_quarto(): # placed piece created a winning board
                        return other_player
                    break  # piece is placed - breaks the loop

                Console.output("Wybrane pole jest zajęte, wybierz inne.")

            Console.clear_view()
            self.next_turn()

        Console.clear_view()
        return None  # game ends without anyoune winning

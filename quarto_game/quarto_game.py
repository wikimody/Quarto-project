import random

from .board import Board
from .piece import Piece


class QuartoGame:
    def __init__(self, player1, player2):
        self._players = [player1, player2]
        self._turn = random.randint(0, 1)
        self._avaliable_pieces = [Piece(val) for val in range(16)]
        self._board = Board()

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

    # returns list of pieces in readable format (string)
    def format_avaliable_pieces(self):
        readable_pieces = "|"
        for piece in self._avaliable_pieces:
            piece_value = piece.decimal()
            # column spacing adjusting
            if piece_value < 10:
                readable_pieces += " %d|" % piece_value
            else:
                readable_pieces += "%d|" % piece_value
        readable_pieces += "\n"
        readable_pieces += "|--" * len(self._avaliable_pieces) + "|\n"

        readable_pieces += "|"
        for piece in self._avaliable_pieces:
            readable_pieces += "%d%d|" % (piece.binary()[0], piece.binary()[1])
        readable_pieces += "\n"

        readable_pieces += "|"
        for piece in self._avaliable_pieces:
            readable_pieces += "%d%d|" % (piece.binary()[2], piece.binary()[3])
        readable_pieces += "\n"

        return readable_pieces

    def display_preturn_state(self):
        print(self._board)
        print("Kolej gracza %s" % self.current_player())
        print("Dostępne figury: \n%s" % self.format_avaliable_pieces())

    def display_postturn_state(self):
        print(self._board)
        print("Gracz %s stawia figurę." % self.other_player())

    def start(self):
        # Game is going on while there are pieces to choose from
        while len(self._avaliable_pieces):
            current_player = self.current_player()  # player that picks a piece
            other_player = self.other_player()  # player that places it down

            self.display_preturn_state()

            # current player chooses piece for the opponent
            piece_value = input("Wybierz figurę dla przeciwnika: ")
            piece = self.find_piece(int(piece_value)) if piece_value.isnumeric() else None
            while piece == None:
                piece_value = input("Figura o podanej wartości nie istnieje, wybierz inną: ")
                piece = self.find_piece(int(piece_value)) if piece_value.isnumeric() else None
            self._avaliable_pieces.remove(piece)

            self.clear_view()
            self.display_postturn_state()

            print("Otrzymana figura: \n%s" % piece)
            while True:  # loops until piece is correctly placed on board
                row = input("Wybierz rząd (1-4): ")
                while not (row.isnumeric() and 1 <= int(row) <= 4):
                    row = input("Wybrany rząd nie istnieje, ponów wybór: ")
                row = int(row)

                col = input("Wybierz kolumnę (1-4): ")
                while not (col.isnumeric() and 1 <= int(col) <= 4):
                    col = input("Wybrana kolumna nie istnieje, ponów wybór: ")
                col = int(col)

                if self._board.is_avaliable(row, col):  # True if piece can be correctly placed
                    self._board.place(piece, row, col)
                    quarto_call = input("Czy chcesz zawołać Quarto? Wybierz TAK/NIE [t/n]: ")
                    while not quarto_call.upper() in ("T", "TAK", "N", "NIE"):
                        quarto_call = input("Odpowiedź musi być w formacie TAK lub NIE [t/n]: ")
                    if quarto_call.upper() in ("T", "TAK"):
                        if self._board.is_quarto():
                            return other_player  # players successfuly calls Quarto and wins the game
                        input("Podana figura nie tworzy Quarto, wciśnij Enter, aby kontynuować...")
                    break  # piece is placed - breaks the loop

                print("Wybrane pole jest zajęte, wybierz inne.")

            self.clear_view()
            self.next_turn()

        self.clear_view()
        return None  # game ends without anyoune winning

    def clear_view(self):
        print("\n" * 28)

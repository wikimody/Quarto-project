from interactions.debug_console import Console
from .piece import Piece


class QuartoGame:
    def __init__(self, board, player1, player2, turn=0):
        self._board = board
        self._players = [player1, player2]
        self._turn = turn
        self._avaliable_pieces = [Piece(val) for val in range(16)]

    def switch_player(self):
        self._turn = (self._turn + 1) % 2

    def current_player(self):
        return self._players[self._turn]

    # returns piece with given value (returns None if not found)
    def get_piece(self, piece_value):
        for piece in self._avaliable_pieces:
            if piece.decimal() == piece_value:
                return piece
        return None

    def avaliable_pieces_values(self):
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

    def display_to_place_piece(self, piece):
        Console.clear_view()
        Console.output(self._board)
        Console.output(f"{str(self.current_player())} stawia pionek \u2116{piece.decimal()}: \n{piece}")

    def display_to_choose_piece(self):
        Console.clear_view()
        Console.output(self._board)
        Console.output(
            f"{str(self.current_player())} wybiera dla przeciwnika jednego z pozostałych pionków:\n{self.format_avaliable_pieces()}")

    def start(self):
        self.display_to_choose_piece()
        chosen_piece = self.get_piece(
            self.current_player().choose_piece(self.avaliable_pieces_values()))  # choose first piece for opponent
        self.switch_player()

        # Game is going on while there are pieces to choose from
        while len(self._avaliable_pieces):
            Console.output(f"Wybrano pionek \u2116{chosen_piece.decimal()}:\n{chosen_piece}")
            self.display_to_place_piece(chosen_piece)
            row, col = self.current_player().where_place_piece(chosen_piece,
                                                               self._board)  # this should return correct row and col
            self._board.place(chosen_piece, row, col)
            self._avaliable_pieces.remove(chosen_piece)

            if self._board.is_quarto():  # placed piece created a winning board
                Console.clear_view()
                Console.output(self._board)
                return self.current_player()

            self.display_to_choose_piece()  # current player chooses piece for the opponent
            chosen_piece = self.get_piece(self.current_player().choose_piece(
                self.avaliable_pieces_values()))  # zauważyłem że bot2 tutaj czasem zwraca None

            self.switch_player()

        Console.clear_view()
        Console.output(self._board)
        return None  # game ends without anyone winning

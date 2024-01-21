from interactions.debug_console import Console
from .piece import Piece


class QuartoGame:
    def __init__(self, board, player1, player2, turn=0):
        self._board = board
        self._players = [player1, player2]
        self._turn = turn
        self._avaliable_pieces = [Piece(val) for val in range(16)]

    def switch_turn(self):
        self._turn = (self._turn + 1) % 2

    def current_player(self):
        return self._players[self._turn]

    def opponent_player(self):
        return self._players[(self._turn + 1) % 2]

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

    def display_preturn_state(self):
        Console.output(self._board)
        Console.output(f"Gracz {str(self.current_player()).upper()} wybiera figurę")
        Console.output(f"Dostępne figury: \n{self.format_avaliable_pieces()}")

    def display_postturn_state(self):
        Console.output(self._board)
        Console.output(f"Gracz {str(self.opponent_player()).upper()} stawia figurę.")

    def start(self):
        # Game is going on while there are pieces to choose from
        while len(self._avaliable_pieces):
            current_player = self.current_player()  # player that picks a piece
            other_player = self.opponent_player()  # player that places it down

            self.display_preturn_state()

            # current player chooses piece for the opponent
            piece_value = current_player.choose_piece(self.avaliable_pieces_values())
            piece = self.get_piece(piece_value)
            self._avaliable_pieces.remove(piece)

            Console.clear_view()
            self.display_postturn_state()

            Console.output(f"Figura do postawienia: \n{piece}")
            while True:  # loops until piece is correctly placed on board
                row, col = other_player.where_place_piece(piece)

                if self._board.is_avaliable(row, col):  # True if piece can be correctly placed
                    self._board.place(piece, row, col)
                    if self._board.is_quarto():  # placed piece created a winning board
                        return other_player
                    break  # piece is placed - breaks the loop

                Console.output("Wybrane pole jest zajęte, wybierz inne.")

            Console.clear_view()
            self.switch_turn()

        Console.clear_view()
        return None  # game ends without anyoune winning

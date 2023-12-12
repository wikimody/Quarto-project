from .piece import Piece


class Board:
    def __init__(self):  # creates board filled with empty pieces
        self._board = [[Piece(None) for tile in range(4)] for row in range(4)]

    def has_empty_tiles(self):
        for row in self._board:
            for tile in row:
                if tile.is_idle():
                    return True
        return False

    # user inputs row and col values in [1-4] format
    def is_avaliable(self, row, col):
        return self._board[row - 1][col - 1].is_idle()

    def place(self, piece, row, col):
        self._board[row - 1][col - 1] = piece

    # returns True if piece creates a Quarto, False otherwise
    def is_validating(self, piece):  # Temporarly false
        return False

    def format(self):  # returns board in string format "t t ... t t" (t - 16 tile values)
        " ".join(" ".join(str(tile.decimal()) for tile in row) for row in _board)

    def __str__(self):
        readable_board = "#|1111|2222|3333|4444|\n"
        readable_board += "#|----|----|----|----|\n"

        for m in range(4):
            readable_row = "%d|" % (m + 1)
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_idle():
                    readable_row += "    |"
                else:
                    piece_binary = piece.binary()
                    readable_row += " %d%d |" % (piece_binary[0], piece_binary[1])
            readable_row += "\n"
            readable_row += "%d|" % (m + 1)
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_idle():
                    readable_row += "    |"
                else:
                    piece_binary = piece.binary()
                    readable_row += " %d%d |" % (piece_binary[2], piece_binary[3])
            readable_row += "\n"
            readable_row += "#|----|----|----|----|\n"
            readable_board += readable_row

        return readable_board

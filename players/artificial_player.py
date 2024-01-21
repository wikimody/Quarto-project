from .player import Player


# Zaimplementowałem od razu najgłupszego możliwego bota
class ArtificialPlayer(Player):
    def __init__(self, level, board):
        self._level = level
        self._board = board

    def choose_piece(self, pieces):  # pieces - lista wartości pionów (decymalna)
        # W tym miejscu bot wybiera, którą figurę przekazać drugiemu graczowi
        # Podanie niepoprawnej wartości może poskutkować błędem programu
        # oczekiwana wartość: jedna z wartości listy pieces
        return pieces[0]

    def where_place_piece(self, piece):  # piece - obiekt klasy Piece
        # W tym miejscu bot wybiera, gdzie postawić figurę
        # Podanie niepoprawnej wartości poskutkuje ponownym wywołaniem funkcji (możliwa nieskończona pętla)
        # oczekiwana wartość: krotka (a, b) [1 <= a,b <= 4]

        for row in range(1, 5):
            for col in range(1, 5):
                if self._board.is_avaliable(row, col):
                    return (row, col)

    def __str__(self):
        return "Bot (poziom %d)" % self._level

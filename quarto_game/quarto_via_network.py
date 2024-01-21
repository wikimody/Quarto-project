from interactions.console import Console
from .quarto_game import QuartoGame


class QuartoViaNetwork(QuartoGame):
    def __init__(self, board, player1, player2, turn=0):
        # player1 - local player; player2 - connected remote player
        super().__init__(board, player1, player2, turn)

    def start(self):
        local = self._players[0]
        remote = self._players[1]._connected_device

        Console.clear_view()
        if self._turn == 0:
            self.display_to_choose_piece()
            chosen_piece = local.choose_piece(self.avaliable_pieces_values())
            remote.send_message(str(chosen_piece))
            Console.clear_view()
        else:
            self.switch_player()
            Console.output("Czekamy na ruch twojego przeciwnika...")
            Console.output("NIC NIE WPISUJ!!!")
            piece_to_place = int(remote.receive_message())
            Console.clear_view()

            self.display_to_place_piece(self.get_piece(piece_to_place))
            row, col = local.where_place_piece(None)
            self._board.place(self.get_piece(piece_to_place), row, col)
            self._avaliable_pieces.remove(self.get_piece(piece_to_place))

            Console.clear_view()

            self.display_to_choose_piece()
            chosen_piece_val = local.choose_piece(self.avaliable_pieces_values())

            message = f"{piece_to_place} {row} {col} {chosen_piece_val}"
            remote.send_message(message)
            Console.clear_view()

        # Game is going on while there are pieces to choose from
        while len(self._avaliable_pieces):
            Console.clear_view()
            Console.output("Czekamy na ruch twojego przeciwnika...")
            Console.output("NIC NIE WPISUJ!!!")
            placed_piece, at_row, at_col, piece_to_place = map(int, remote.receive_message().split())
            self._board.place(self.get_piece(placed_piece), at_row, at_col)
            self._avaliable_pieces.remove(self.get_piece(placed_piece))
            Console.clear_view()

            if self._board.is_quarto():
                Console.output(self._board)
                return self._players[1]

            self.display_to_place_piece(self.get_piece(piece_to_place))
            row, col = local.where_place_piece(board=self._board)
            self._board.place(self.get_piece(piece_to_place), row, col)
            self._avaliable_pieces.remove(self.get_piece(piece_to_place))

            Console.clear_view()

            if self._board.is_quarto():
                Console.output(self._board)
                message = f"{piece_to_place} {row} {col} {-1}"
                remote.send_message(message)
                return local

            self.display_to_choose_piece()
            chosen_piece_val = local.choose_piece(self.avaliable_pieces_values())

            message = f"{piece_to_place} {row} {col} {chosen_piece_val}"
            remote.send_message(message)

        Console.clear_view()
        return None  # game ends without anyoune winning

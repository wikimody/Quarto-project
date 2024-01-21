from .quarto_game import QuartoGame
from interactions.console import Console
from players.remote_player import RemotePlayer
from networking.server import Server
from networking.client import Client

class QuartoViaNetwork(QuartoGame):
    def __init__(self, board, player1, player2, turn=0): # player1 - local player; player2 - remote player
        super().__init__(board, player1, player2, turn)

    def start(self):
        local = self._players[0]
        remote = self._players[1]._connected_device

        Console.clear_view()
        if self._turn == 0:
            self.display_preturn_state()
            chosen_piece = local.choose_piece(self.avaliable_piece_values())
            remote.send_message(str(chosen_piece))
            Console.clear_view()
        else:
            Console.output("Czekamy na ruch oponenta...")
            Console.output("NIC NIE WPISUJ!!!")
            piece_to_place = int(remote.receive_message())
            Console.clear_view()

            self.display_postturn_state()
            Console.output(f"Otrzymana figura: \n{self.find_piece(piece_to_place)}")
            row, col = local.place_piece(None)
            self._board.place(self.find_piece(piece_to_place), row, col)
            self._avaliable_pieces.remove(self.find_piece(piece_to_place))

            Console.clear_view()

            self.display_preturn_state()
            chosen_piece_val = local.choose_piece(self.avaliable_piece_values())

            message = f"{piece_to_place} {row} {col} {chosen_piece_val}"
            remote.send_message(message)
            Console.clear_view()



        # Game is going on while there are pieces to choose from
        while len(self._avaliable_pieces):
            Console.output("Czekamy na ruch oponenta...")
            Console.output("NIC NIE WPISUJ!!!")
            placed_piece, at_row, at_col, piece_to_place = map(int, remote.receive_message().split())
            Console.clear_view()
            print(f"OTRZYMANE DANE: {placed_piece}, {at_row}, {at_col}, {piece_to_place}")

            self._board.place(self.find_piece(placed_piece), at_row, at_col)
            self._avaliable_pieces.remove(self.find_piece(placed_piece))

            self.display_postturn_state()
            Console.output(f"Otrzymana figura: \n{self.find_piece(piece_to_place)}")
            row, col = local.place_piece(None)
            self._board.place(self.find_piece(piece_to_place), row, col)
            self._avaliable_pieces.remove(self.find_piece(piece_to_place))

            Console.clear_view()

            self.display_preturn_state()
            chosen_piece_val = local.choose_piece(self.avaliable_piece_values())

            message = f"{piece_to_place} {row} {col} {chosen_piece_val}"
            remote.send_message(message)


            Console.clear_view()


        Console.clear_view()
        return None  # game ends without anyoune winning
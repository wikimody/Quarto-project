from .player import Player
from quarto_game.piece import Piece
import cpp_bots.cpp_adapter as cppA
import time
from quarto_game.board import Board


class ArtificialPlayer(Player):
    def __init__(self, level : int, board : Board) -> None:
        self._level = level
        self._board = board
        self._piece_number = -1

    def choose_piece(self, pieces : list(int)) -> int: 
        if self._piece_number == -1:
            return time.time() % 16 # XD - ale jest to jakaś losowość
        return self._piece_number 

    def place_piece(self, piece : Piece) -> list(int, int): 
        args = cppA.generate_args((self._board), piece.decimal())
        result = cppA.execute_cpp(f"../cpp_bots/bin/bot{self._level}",  args)
        result_list = cppA.receive_args(result)
        self._piece_number = result_list[2]
        return(result_list[0], result_list[1])

    def __str__(self) -> str:
        return "Bot (poziom %d)" % self._level

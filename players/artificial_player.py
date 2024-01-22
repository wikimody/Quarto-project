from .player import Player
from quarto_game.piece import Piece
import cpp_bots.cpp_adapter as cppA
from quarto_game.board import Board
import time



class ArtificialPlayer(Player):
    def __init__(self, name : str, path : str) -> None:
        self._name = name
        self._path = path
        self._piece_number = -1

    def choose_piece(self, pieces : list) -> int: 
        if self._piece_number == -1:        # jeśli bot zaczyna to musi wylosować pierwszego piona
            return pieces[int(time.time() % 16)] # XD - ale jest to jakaś losowość (tak wiem, że jest random.choice)
        return self._piece_number 

    def where_place_piece(self, piece : Piece, board : Board) -> list:
        args = cppA.generate_args(board, piece.decimal()) # generujemy argument dla pliku cpp
        result = cppA.execute_cpp(self._path,  args)  # wykonujemy plik
        result_list = cppA.receive_args(result) # wyciągamy wyniki odpowiednio przetworzone
        self._piece_number = result_list[2] # wybrany przez bot pionek zapisujemy, żeby w odpowiednim momencie zwrócić
        return(result_list[0], result_list[1]) # zwracamy wybrane miejsce

    def __str__(self) -> str:
        return self._name

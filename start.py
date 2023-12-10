import random

class Player:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class Piece:
    def __init__(self, piece_value):
        if piece_value == None or piece_value < 0 or 16 <= piece_value: # empty piece case
            self._value = -1
            self._bin_value = None
            return
        
        self._value = piece_value

        self._bin_value = [0, 0, 0, 0]
        if piece_value >= 8: # color
            self._bin_value[0] = 1
            piece_value -= 8
        if piece_value >= 4: # shape
            self._bin_value[1] = 1
            piece_value -= 4
        if piece_value >= 2: # filling
            self._bin_value[2] = 1
            piece_value -= 2
        self._bin_value[3] = piece_value # height

    def is_idle(self):
        return self._bin_value == None

    def is_white(self):
        return self._bin_value[0] == 1

    def is_circle(self):
        return self._bin_value[1] == 1

    def is_filled(self):
        return self._bin_value[2] == 1

    def is_high(self):
        return self._bin_value[3] == 1

    def decimal(self): # empty pieces return -1
        return self._value

    def binary(self): # empty pieces return None
        return self._bin_value

    def __str__(self):
        return f"{self._bin_value[0]}{self._bin_value[1]}\n{self._bin_value[2]}{self._bin_value[3]}"

class Board:
    def __init__(self): # creates board filled with empty pieces
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
    def is_validating(self, piece): # Temporarly false
        return False

    def format(self): # returns board in string format "t t ... t t" (t - 16 tile values)
        " ".join(" ".join(str(tile.decimal()) for tile in row) for row in _board)
    
    def __str__(self):
        readable_board  = "#|1111|2222|3333|4444|\n"
        readable_board += "#|----|----|----|----|\n"
        
        for m in range(4):
            readable_row = "%d|" % (m+1)
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_idle():
                    readable_row += "    |"
                else:
                    piece_binary = piece.binary()
                    readable_row += " %d%d |" % (piece_binary[0], piece_binary[1])
            readable_row += "\n"
            readable_row += "%d|" % (m+1)
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_idle():
                    readable_row += "    |"
                else:
                    piece_binary = piece.binary()
                    readable_row += " %d%d |" % (piece_binary[2], piece_binary[3])
            readable_row += "\n"
            readable_row +=  "#|----|----|----|----|\n"
            readable_board += readable_row

        return readable_board

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
                readable_pieces += "%d|"  % piece_value
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
            current_player = self.current_player() # player that picks a piece
            other_player = self.other_player() # player that places it down
            
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
            while True: # loops until piece is correctly placed on board
                row = input("Wybierz rząd (1-4): ")
                while not (row.isnumeric() and 1 <= int(row) <= 4):
                    row = input("Wybrany rząd nie istnieje, ponów wybór: ")
                row = int(row)
                
                col = input("Wybierz kolumnę (1-4): ")
                while not (col.isnumeric() and 1 <= int(col) <= 4):
                    col = input("Wybrana kolumna nie istnieje, ponów wybór: ")
                col = int(col)
                
                if self._board.is_avaliable(row, col): # True if piece can be correctly placed
                    self._board.place(piece, row, col)
                    quarto_call = input("Czy chcesz zawołać Quarto? Wybierz TAK/NIE [t/n]: ")
                    while not quarto_call.upper() in ("T", "TAK", "N", "NIE"):
                        quarto_call = input("Odpowiedź musi być w formacie TAK lub NIE [t/n]: ")
                    if quarto_call.upper() in ("T", "TAK"):
                        if self._board.is_validating(piece):
                            return other_player # players successfuly calls Quarto and wins the game
                        input("Podana figura nie tworzy Quarto, wciśnij Enter, aby kontynuować...")
                    break # piece is placed - breaks the loop
            
                print("Wybrane pole jest zajęte, wybierz inne.")

            self.clear_view()
            self.next_turn()

        self.clear_view()
        return None # game ends without anyoune winning
    
    def clear_view(self):
        print("\n" * 28)


if __name__ == '__main__':
    # player1 = Player(input("Wprowadź nazwę pierwszego gracza: "))
    # player2 = Player(input("Wprowadź nazwę drugiego gracza: "))
    game = QuartoGame(Player("A"), Player("B"))
    winner = game.start()
    if (winner != None):
        print("Zwyciężył gracz %s" % winner)
    else:
        print("Gra zakończyła się remisem")

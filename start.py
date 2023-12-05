import random

class Player:
    def __init__(self, name):
        self._name = name
        self._board = None

    def join_board(self, board):
        self._board = board

    def place(self, piece):
        print("Otrzymana figura: \n%s" % piece)
        while True:
            row = input("Wybierz rząd (1-4): ")
            while not (row.isnumeric() and 1 <= int(row) <= 4):
                row = input("Wybrany rząd nie istnieje, ponów wybór: ")
            row = int(row)
            
            col = input("Wybierz kolumnę (1-4): ")
            while not (col.isnumeric() and 1 <= int(col) <= 4):
                col = input("Wybrana kolumna nie istnieje, ponów wybór: ")
            col = int(col)
            
            if self._board.is_avaliable(row, col):
                self._board.place(piece, row, col)
                quarto_call = input("Czy chcesz zawołać quatro? Wybierz TAK/NIE [t/n]: ")
                while not quarto_call.upper() in ("T", "TAK", "N", "NIE"):
                    quarto_call = input("Odpowiedź musi być w formacie TAK lub NIE [t/n]: ")
                if quarto_call.upper() in ("T", "TAK"):
                    if self._board.is_winning(piece):
                        return True
                    print("Podana figura nie tworzy Quatro")
                return False
            
            print("Wybrane pole jest zajęte, wybierz inne.")

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

    def is_empty(self):
        return self._bin_value == None

    def is_white(self):
        return self._bin_value[0] == 1

    def is_circle(self):
        return self._bin_value[1] == 1

    def is_square(self):
        return self._bin_value[2] == 1

    def is_high(self):
        return self._bin_value[3] == 1

    def decimal(self): # empty pieces return -1
        return self._value

    def binary(self): # empty pieces return None
        return self._bin_value

    def __str__(self):
        return "%d%d\n%d%d" % (self._bin_value[0], self._bin_value[1], self._bin_value[2], self._bin_value[3])

class Board:
    def __init__(self): # creates board filled with empty pieces
        self._board = [[Piece(None) for tile in range(4)] for row in range(4)]

    def has_empty_tiles(self):
        for row in self._board:
            for tile in row:
                if tile.is_empty():
                    return True
        return False

    def is_avaliable(self, row, col):
        return self._board[row - 1][col - 1].is_empty()

    def place(self, piece, row, col):
        self._board[row - 1][col - 1] = piece

    def is_winning(self, piece): # Temporarly false
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
                if piece.is_empty():
                    readable_row += "    |"
                else:
                    piece_binary = piece.binary()
                    readable_row += " %d%d |" % (piece_binary[0], piece_binary[1])
            readable_row += "\n"
            readable_row += "%d|" % (m+1)
            for n in range(4):
                piece = self._board[m][n]
                if piece.is_empty():
                    readable_row += "    |"
                else:
                    piece_binary = piece.binary()
                    readable_row += " %d%d |" % (piece_binary[2], piece_binary[3])
            readable_row += "\n"
            readable_row +=  "#|----|----|----|----|\n"
            readable_board += readable_row

        return readable_board

class Game:
    def __init__(self, player1, player2):
        self._players = [player1, player2]
        self._turn = random.randint(0, 1)
        self._avaliable_pieces = [Piece(val) for val in range(16)]
        self._board = Board()
        player1.join_board(self._board)
        player2.join_board(self._board)

    def next_turn(self):
        self._turn = (self._turn + 1) % 2

    def current_player(self):
        return self._players[self._turn]

    def other_player(self):
        return self._players[(self._turn + 1) % 2]

    def remove_piece(self, piece_ord):
        self._avaliable_pieces = self._avaliable_pieces[:piece_ord]

    def format_avaliable_pieces(self): # returns list of pieces in readable format (string)
        number_of_pieces = len(self._avaliable_pieces)

        readable_pieces = "|"
        for i in range(1, number_of_pieces+1): # column spacing
            if i < 10:
                readable_pieces += " %d|" % i
            else:
                readable_pieces += "%d|"  % i
        readable_pieces += "\n"
        readable_pieces += "|--" * number_of_pieces + "|\n"

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
        while self._board.has_empty_tiles():
            current_player = self.current_player()
            other_player = self.other_player()
            
            self.display_preturn_state()
            
            piece_ord = input("Wybierz figurę dla przeciwnika: ")
            while not (piece_ord.isnumeric() and 1 <= int(piece_ord) <= len(self._avaliable_pieces)):
                piece_ord = input("Podana figura nie istnieje, wybierz inną: ")
            piece_ord = int(piece_ord) - 1

            chosen_piece = self._avaliable_pieces[piece_ord]
            del self._avaliable_pieces[piece_ord]
            
            self.clear_view()
            self.display_postturn_state()
            
            quarto_call = other_player.place(chosen_piece)
            if quarto_call:
                return other_player

            self.clear_view()
            self.next_turn()

        self.clear_view()
        return None
    
    def clear_view(self):
        print("\n" * 28)


if __name__ == '__main__':
    # player1 = Player(input("Wprowadź nazwę pierwszego gracza: "))
    # player2 = Player(input("Wprowadź nazwę drugiego gracza: "))
    game = Game(Player("A"), Player("B"))
    winner = game.start()
    if (winner != None):
        print("Zwyciężył gracz %s" % winner)
    else:
        print("Gra zakończyła się remisem")

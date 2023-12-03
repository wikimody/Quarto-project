def print_board(board):
    print("-------------")
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print("\n-------------")


def print_available_pieces(pieces):
    print("Available Pieces:")
    sorted_pieces = sorted(pieces)
    for piece in sorted_pieces:
        print(piece, end=" ")


def is_quarto(board):
    return False


if __name__ == '__main__':
    pieces = {x for x in range(16)}
    board = [[-1 for _ in range(4)] for _ in range(4)]
    print_board(board)
    print("First player:")
    print(print_available_pieces(pieces))
    chosen_piece = int(input("Choose availible piece for your enemy:"))
    players_number = "Second"
    print("\n" * 20)
    while True:
        print(players_number + " player:")
        print("Place the piece #" + str(chosen_piece) + " on the board")
        print_board(board)
        row = int(input("Enter the row (0-3) to place the piece:"))
        column = int(input("Enter the column (0-3) to place the piece:"))
        board[row][column] = chosen_piece
        pieces.remove(chosen_piece)
        if is_quarto(board):
            print(players_number + " player has won!!!")
            break
        print_board(board)
        print(print_available_pieces(pieces))
        chosen_piece = int(input("Now choose availible piece for your enemy:"))
        print("\n" * 20)
        if players_number == "Second":
            players_number = "First"
        else:
            players_number = "Second"

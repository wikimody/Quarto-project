from players.local_player import LocalPlayer
from players.artificial_player import ArtificialPlayer
from quarto_game.board import Board
from quarto_game.quarto_game import QuartoGame
from interactions.debug_console import Console

def start_menu(page = 1):
    if page == 1:
        Console.output("Witaj w grze Quarto!") # Wyświetlanie powitalnego komunikatu
        Console.output("1. Graj z człowiekiem")
        Console.output("2. Graj z botem 1")
        Console.output("3. Graj z botem 2")
        Console.output("4. Graj z botem 3")
        Console.output("5. Starcie botów")
        Console.output("6. Zasady gry")
        Console.output("7. Wyjdź z gry")
    else:
        Console.output("Wybierz poziomy zaawansowania botów")
        Console.output("1. P1 vs P1")
        Console.output("2. P1 vs P2")
        Console.output("3. P1 vs P3")
        Console.output("4. P2 vs P2")
        Console.output("5. P2 vs P3")
        Console.output("6. P3 vs P3")
        Console.output("7. Wróć")

def play_with_human():
    Console.clear_view()
    board = Board()
    player1 = LocalPlayer(Console.input_text("Wprowadź nazwę pierwszego gracza: "))
    player2 = LocalPlayer(Console.input_text("Wprowadź nazwę drugiego gracza: "))
    game = QuartoGame(board, player1, player2)
    winner = game.start()
    if (winner != None):
        Console.output("Zwyciężył gracz %s" % winner)
    else:
        Console.output("Gra zakończyła się remisem")

def play_with_bot(level):
    Console.clear_view()
    board = Board()
    player1 = LocalPlayer(Console.input_text("Wprowadź swoją nazwę gracza: "))
    player2 = ArtificialPlayer(level, board)
    game = QuartoGame(board, player1, player2)
    winner = game.start()
    if (winner == player1):
        Console.output("Zwyciężyłeś")
    elif (winner == player2):
        Console.output("Zwyciężył bot")
    else:
        Console.output("Gra zakończyła się remisem")

def start_bot_battle(level):
    Console.clear_view()
    board = Board()
    player1, player2 = None, None
    
    if level in [1, 2, 3]:
        player1 = ArtificialPlayer(1, board)
    elif level in [4, 5]:
        player1 = ArtificialPlayer(2, board)
    elif level == 6:
        player1 = ArtificialPlayer(3, board)

    if level == 1:
        player2 = ArtificialPlayer(1, board)
    elif level in [2, 4]:
        player2 = ArtificialPlayer(2, board)
    elif level in [3, 5, 6]:
        player2 = ArtificialPlayer(3, board)

    game = QuartoGame(board, player1, player2)
    winner = game.start()
    if (winner != None):
        Console.output("Zwyciężył bot %s" % winner)
    else:
        Console.output("Gra zakończyła się remisem")
        
def show_rules():
    Console.output("Zasady gry Quarto: https://www.ultraboardgames.com/quarto/game-rules.php")

if __name__ == "__main__":
    while True:
        start_menu(1)
        choice = Console.input_number_in_range("Wybierz opcję (1-7): ", 1, 7)
        if choice == 1:
            play_with_human()
        elif choice in [2, 3, 4]:
            play_with_bot(choice-1)
        elif choice == 5:
            start_menu(2)
            choice = Console.input_number_in_range("Wybierz opcję (1-7): ", 1, 7)
            if 1 <= choice <= 6:
                start_bot_battle(choice)
            elif choice == 7:
                Console.clear_view()
                continue
        elif choice == 6:
            Console.clear_view()
            show_rules()
            Console.output()
        elif choice == 7:
            Console.output("Dziękujemy za grę. Do widzenia!")
            break

        # Po zakończeniu wybranej opcji, wykonaj grę Quarto
        # Program wraca do menu po zakończeniu gry

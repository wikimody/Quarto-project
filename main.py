from interactions.debug_console import Console
from networking.client import Client
from networking.server import Server
from players.artificial_player import ArtificialPlayer
from players.local_player import LocalPlayer
from players.remote_player import RemotePlayer
from quarto_game.board import Board
from quarto_game.menu import Menu
from quarto_game.quarto_game import QuartoGame
from quarto_game.quarto_via_network import QuartoViaNetwork


def play_with_human():
    Console.clear_view()
    board = Board()
    player1 = LocalPlayer(Console.input_text("Wprowadź nazwę pierwszego gracza: "))
    player2 = LocalPlayer(Console.input_text("Wprowadź nazwę drugiego gracza: "))
    game = QuartoGame(board, player1, player2)
    winner = game.start()
    if winner is not None:
        Console.output("Zwyciężył gracz %s" % winner)
    else:
        Console.output("Gra zakończyła się remisem")
    input("ENTER żeby kontynuować...")


def play_via_network():
    Console.clear_view()
    board = Board()
    if Console.input_yes_or_no("Czy ty zaczynasz grę?"):
        Console.clear_view()
        player1 = LocalPlayer(Console.input_text("Wprowadź swój nickname: "))
        player2 = RemotePlayer(Server())
        game = QuartoViaNetwork(board, player1, player2, 0)
    else:
        Console.clear_view()
        player1 = LocalPlayer(Console.input_text("Wprowadź swój nickname: "))
        Console.output("Wprowadź dane hosta:")
        host = Console.input_text("IP / localhost: ")
        port = Console.input_number_in_range("Port: ", 1000, 99999)
        player2 = RemotePlayer(Client(host, port))
        game = QuartoViaNetwork(board, player1, player2, 1)
    winner = game.start()
    if winner == player1:
        Console.output("Gratulacje!!! Zwyciężyłeś")
    elif winner == player2:
        Console.output("Niestety przegrałeś")
    else:
        Console.output("Gra zakończyła się remisem")
    player2._connected_device.close()
    input("ENTER żeby kontynuować...")


def play_with_bot(bot_name):
    Console.clear_view()
    board = Board()
    player1 = LocalPlayer(Console.input_text("Wprowadź swoją nazwę gracza: "))
    player2 = ArtificialPlayer(name=f"{bot_name}", path=f"cpp_bots/bin/{bot_name}")
    game = QuartoGame(board, player1, player2)
    winner = game.start()
    if winner == player1:
        Console.output("Zwyciężyłeś")
    elif winner == player2:
        Console.output("Zwyciężył bot")
    else:
        Console.output("Gra zakończyła się remisem")
    input("ENTER żeby kontynuować...")


def start_bot_battle(bot1_name, bot2_name):
    Console.clear_view()
    board = Board()
    if bot1_name != bot2_name:
        player1 = ArtificialPlayer(name=f"{bot1_name}", path=f"cpp_bots/bin/{bot1_name}")
        player2 = ArtificialPlayer(name=f"{bot2_name}", path=f"cpp_bots/bin/{bot2_name}")
    else:
        player1 = ArtificialPlayer(name=f"{bot1_name} #1", path=f"cpp_bots/bin/{bot1_name}")
        player2 = ArtificialPlayer(name=f"{bot2_name} #2", path=f"cpp_bots/bin/{bot2_name}")

    game = QuartoGame(board, player1, player2)
    winner = game.start()
    if winner is not None:
        Console.output(f"Zwyciężył {winner}")
    else:
        Console.output("Gra zakończyła się remisem")
    input("ENTER żeby kontynuować...")


def show_rules():
    Console.output("Zasady gry Quarto: https://www.ultraboardgames.com/quarto/game-rules.php")
    input("ENTER żeby kontynuować...")

def choose_one_bot():  # helper function
    BOTS_NUMBER = 3

    Console.output("\nWybierz bota z którym chcesz zagrać:")
    for index in range(1, BOTS_NUMBER + 1):
        Console.output(f"{index}. Bot {index}")
    Console.output("0. Powrót do menu")
    choice = Console.input_number_in_range(f"Wybierz opcję (0-{BOTS_NUMBER}): ", 0, BOTS_NUMBER)
    if choice == 0:
        return

    play_with_bot(f"bot{choice}.exe")


def choose_two_bots():  # helper function
    BOTS_NUMBER = 3

    Console.output("\nWybierz pierwszego bota:")
    for index in range(1, BOTS_NUMBER + 1):
        Console.output(f"{index}. Bot {index}")
    Console.output("0. Powrót do menu")
    first_bot = Console.input_number_in_range(f"Wybierz opcję (0-{BOTS_NUMBER}): ", 0, BOTS_NUMBER)
    if first_bot == 0:
        return

    Console.output("\nWybierz drugiego bota:")
    for index in range(1, BOTS_NUMBER + 1):
        Console.output(f"{index}. Bot {index}")
    Console.output("0. Powrót do menu")
    second_bot = Console.input_number_in_range(f"Wybierz opcję (0-{BOTS_NUMBER}): ", 0, BOTS_NUMBER)
    if second_bot == 0:
        return

    start_bot_battle(f"bot{first_bot}.exe", f"bot{second_bot}.exe")


# Run menu
if __name__ == "__main__":
    # Create main menu instance
    main_menu = Menu()
    main_menu.add_option("Graj z człowiekiem (lokalnie)", play_with_human)
    main_menu.add_option("Graj z człowiekiem (przez sieć)", play_via_network)
    main_menu.add_option("Graj z botem", choose_one_bot)
    main_menu.add_option("Starcie botów", choose_two_bots)
    main_menu.add_option("Zasady gry", show_rules)

    main_menu.run()

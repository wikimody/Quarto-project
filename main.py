from players.local_player import LocalPlayer
from quarto_game.quarto_game import QuartoGame

if __name__ == '__main__':
    # player1 = Player(input("Wprowadź nazwę pierwszego gracza: "))
    # player2 = Player(input("Wprowadź nazwę drugiego gracza: "))
    game = QuartoGame(LocalPlayer("A"), LocalPlayer("B"))
    winner = game.start()
    if (winner != None):
        print("Zwyciężył gracz %s" % winner)
    else:
        print("Gra zakończyła się remisem")

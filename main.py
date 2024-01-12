from players.local_player import LocalPlayer 
from quarto_game.quarto_game import QuartoGame
from interactions.console import Console

def start_menu():
    Console.clear_view()   # Czyszczenie ekranu konsoli
    Console.output("Witaj w grze Quarto!") # Wyświetlanie powitalnego komunikatu
    Console.output("1. Graj z człowiekiem")
    Console.output("2. Graj z botem 1")
    Console.output("3. Graj z botem 2")
    Console.output("4. Graj z botem 3")
    Console.output("5. Zasady gry")
    Console.output("6. Wyjdź z gry")

def play_with_human():
    Console.output("Rozpoczynamy nową grę z drugim graczem!")  # Wyświetlanie komunikatu rozpoczęcia gry z drugim graczem
    player1_name = input("Wprowadź nazwę pierwszego gracza: ")
    player2_name = input("Wprowadź nazwę drugiego gracza: ")
    game = QuartoGame(LocalPlayer(player1_name), LocalPlayer(player2_name))
    winner = game.start()
    if (winner != None):
        print("Zwyciężył gracz %s" % winner)
    else:
        print("Gra zakończyła się remisem")

def play_with_bot(level):
    Console.output(f"Rozpoczynamy nową grę z botem!")  # Wyświetlanie komunikatu rozpoczęcia gry z botem

def show_rules():
    Console.output("Zasady gry Quarto:")  # Wyświetlanie zasad gry Quarto
    # Opis zasad gry Quarto
    #Plansza Quarto składa się z 4 na 4 pól, co daje 16 pól do umieszczenia kawałków. Istnieje 16 różnych kawałków, z których każdy ma cztery cechy: kształt, kolor, wysokość i wypełnienie. Każda cecha może przyjąć jedną z dwóch wartości. Na przykład kształt może być okrągły lub kwadratowy, kolor może być biały lub czarny, wysokość może być niska lub wysoka, a wypełnienie może być puste lub pełne. Gracze na zmianę wybierają i umieszczają kawałki na plansy. Po umieszczeniu kawałka na planszy, drugi gracz wybiera kolejny kawałek i umieszcza go na planszy. Gra kończy się, gdy jeden z graczy osiągnie czwórkę kawałków w jednej linii, gdzie każdy z nich ma co najmniej jedną cechę wspólną z pozostałymi trzema kawałkami. Linia może być pozioma, pionowa lub ukosna. Gracz, który osiągnął czwórkę w jednej linii, wygrywa grę.

if __name__ == "__main__":
    while True:
        start_menu()

        try:
            choice = Console.input_number_in_range("Wybierz opcję (1-6): ", 1, 6)
            if choice == 1:
                play_with_human()
            elif choice in [2, 3, 4]:
                play_with_bot(choice)
            elif choice == 5:
                show_rules()
            elif choice == 6:
                Console.output("Dziękujemy za grę. Do widzenia!")
                break
            else:
                Console.output("Podaj numer opcji.")
        except ValueError:
            Console.output("Podaj numer opcji.")

        # Po zakończeniu wybranej opcji, wykonaj grę Quarto
        # Program wraca do menu po zakończeniu gry

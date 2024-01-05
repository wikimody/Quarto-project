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

def play_with_bot(level):
    Console.output(f"Rozpoczynamy nową grę z botem!")  # Wyświetlanie komunikatu rozpoczęcia gry z botem

def show_rules():
    Console.output("Zasady gry Quarto:")  # Wyświetlanie zasad gry Quarto
    # Opis zasad gry Quarto
    #Plansza Quarto składa się z 4 na 4 pól, co daje 16 pól do umieszczenia kawałków. Istnieje 16 różnych kawałków, z których każdy ma cztery cechy: kształt, kolor, wysokość i wypełnienie. Każda cecha może przyjąć jedną z dwóch wartości. Na przykład kształt może być okrągły lub kwadratowy, kolor może być biały lub czarny, wysokość może być niska lub wysoka, a wypełnienie może być puste lub pełne. Gracze na zmianę wybierają i umieszczają kawałki na plansy. Po umieszczeniu kawałka na planszy, drugi gracz wybiera kolejny kawałek i umieszcza go na planszy. Gra kończy się, gdy jeden z graczy osiągnie czwórkę kawałków w jednej linii, gdzie każdy z nich ma co najmniej jedną cechę wspólną z pozostałymi trzema kawałkami. Linia może być pozioma, pionowa lub ukosna. Gracz, który osiągnął czwórkę w jednej linii, wygrywa grę.

    
while True:
    try:
        choice = Console.input_number_in_range("Wybierz opcję (1-6): ", 1, 6)  # Pytanie użytkownika o wybór opcji
        if choice == 1:
            play_with_human() # Rozpoczęcie gry z drugim graczem 
        elif choice in [2, 3, 4]:
            play_with_bot(choice)  # Rozpoczęcie gry z wybranym botem
        elif choice == 5:
            show_rules()  # Wyświetlenie zasad gry
        elif choice == 6:
            Console.output("Dziękujemy za grę. Do widzenia!")  # Wyświetlenie komunikatu kończącego grę
            break
        else:
            Console.output("Podaj numer opcji.")  # Komunikat o wyborze nieprawidłowej opcji
    except ValueError:
        Console.output("Podaj numer opcji.")  # Komunikat o błędzie wartości

if __name__ == "__main__":
    start_menu()

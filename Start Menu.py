def start_menu():
    print("Witaj w grze Quarto!")
    print("1. Graj z człowiekiem")
    print("2. Graj z botem 1")
    print("3. Graj z botem 2")
    print("4. Graj z botem 3")
    print("5. Zasady gry")
    print("6. Wyjdź z gry")

def graj_z_czlowiekiem():
    print("Rozpoczynamy nową grę z drugim graczem!")

def graj_z_botem(poziom):
    print(f"Rozpoczynamy nową grę z botem!")

def show_rules():
    print("Zasady gry Quarto:")


#Plansza Quarto składa się z 4 na 4 pól, co daje 16 pól do umieszczenia kawałków. Istnieje 16 różnych kawałków, z których każdy ma cztery cechy: kształt, kolor, wysokość i wypełnienie. Każda cecha może przyjąć jedną z dwóch wartości. Na przykład kształt może być okrągły lub kwadratowy, kolor może być biały lub czarny, wysokość może być niska lub wysoka, a wypełnienie może być puste lub pełne. Gracze na zmianę wybierają i umieszczają kawałki na plansy. Po umieszczeniu kawałka na planszy, drugi gracz wybiera kolejny kawałek i umieszcza go na planszy. Gra kończy się, gdy jeden z graczy osiągnie czwórkę kawałków w jednej linii, gdzie każdy z nich ma co najmniej jedną cechę wspólną z pozostałymi trzema kawałkami. Linia może być pozioma, pionowa lub ukosna. Gracz, który osiągnął czwórkę w jednej linii, wygrywa grę.

while True:
    try:
        wybor = int(input("Wybierz opcję (1-6): "))
        if wybor == 1:
            graj_z_czlowiekiem()
        elif wybor in [2, 3, 4]:
            graj_z_botem(wybor)
        elif wybor == 5:
            show_rules()
        elif wybor == 6:
            print("Dziękujemy za grę. Do widzenia!")
            break
        else:
            print("Wybierz poprawną opcję (1-6).")
    except ValueError:
        print("Podaj numer opcji.")

if __name__ == "__main__":
    start_menu()

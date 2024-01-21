class Console:
    @staticmethod
    def clear_view():  # Czyszczenie ekranu w trybie debuggera
        print("\n" * 28)

    @staticmethod
    def output(text=""):  # Pisze wysłany tekst
        print(text)

    @staticmethod
    def input_text(question):  # Zadaje pytanie i zwraca odpowiedź
        return input(str(question))

    @staticmethod
    def input_number(question, posible_numbers):  # Zadaje pytanie i zwraca liczbę z przesłanej listy
        entry = input(question)
        while True:
            try:
                number = int(entry)
                if number in posible_numbers:
                    return number
                entry = input(f'Ta liczba nie należy do listy. Podaj liczbę należącą do listy: {posible_numbers} ')
            except ValueError:
                entry = input(f'To nie jest liczba. Podaj liczbę należącą do listy: {posible_numbers} ')

    @staticmethod
    def input_number_in_range(question, begining_of_range,
                              end_of_range):  # Zadaje pytanie i oddaje liczbę w danym zakresie
        entry = input(question)
        while True:
            try:
                number = int(entry)
                if begining_of_range <= number <= end_of_range:
                    return number
                entry = input(
                    f'Ta liczba nie znajduje się w zakresie. Podaj liczbę całkowitą znajdującą się w zakresie: {begining_of_range} do {end_of_range} ')
            except ValueError:
                entry = input(
                    f'To nie jest liczba. Podaj liczbę całkowitą znajdującą się w zakresie: {begining_of_range} do {end_of_range} ')

    @staticmethod
    def input_yes_or_no(question):  # Zadaje pytanie i zwraca True dla tak i False dle nie
        entry = input(f'{question}, odpowiedz T na tak lub N na nie ')
        while True:
            if entry == 't' or entry == 'T':
                return True
            if entry == 'n' or entry == 'N':
                return False
            entry = input('T na tak lub N na nie ')

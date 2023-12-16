import os

class Console:

    @staticmethod
    def is_int(string_to_check):  # Sprawdza czy dany string można zmienić w int, True na tak False na nie
        try:
            a = int(string_to_check)
            return True
        except ValueError:
            return False

    @staticmethod
    def clear_view():  # Czyszczenie ekranu DZIAŁA TYLKO NA LINUXS!!!
        os.system('clear')

    @staticmethod
    def output(text):  # Pisze wysłany tekst
        print(text)

    @staticmethod
    def input_text(question):  # Zadaje pytanie i zwraca odpowiedź
        entry = input(str(question))
        return entry

    @staticmethod
    def input_number(question, posible_numbers):  # Zadaje pytanie i zwraca liczbę z przesłanej listy
        entry = input(question)
        while True:
            if Console.is_int(entry):
                number = int(entry)
                if number in posible_numbers:
                    return number
                else:
                    entry = input(f'Ten numer nie nalerzy do listy. Podaj numer należący do listy: {str(posible_numbers)}')
            else:
                entry = input(f'To nie jest numer. Podaj numer należący do listy: {str(posible_numbers)}')

    @staticmethod
    def input_numer_in_range(question, beginr, endr):  # Zadaje pytanie i oddaje liczbę w danym zakresie
        entry = input(question)
        while True:
            if Console.is_int(entry):
                numer = int(entry)
                if beginr <= numer <= endr:
                    return numer
                else:
                    entry = input(f'Ten numer nie nalerzy do zakresu. Podaj całkowity numer w zakresie: {str(beginr)} do {str(endr)}')
            else:
                entry = input(f'To nie jest numer. Podaj całkowity numer w zakresie: {str(beginr)} do {str(endr)}')

    @staticmethod
    def input_yes_or_no(question):  # Zadaje pytanie i zwraca True dla tak i False dle nie
        entry = input(f'{question}, odpowiedz T na tak lub N na nie')
        while True:
            if entry == 't' or entry == 'T':
                return True
            if entry == 'n' or entry == 'N':
                return False
            entry = input('T na tak lub N na nie')

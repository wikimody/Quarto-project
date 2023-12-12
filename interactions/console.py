import os

class Console:

    @staticmethod
    def is_int(stri):  # czy można zmienić w int
        try:
            a = int(stri)
            return True
        except ValueError:
            return False

    @staticmethod
    def clear_view():  # czyszczenie ekranu TYLKO NA LINUXS!!!
        os.system('clear')

    @staticmethod
    def output(text):  # Print w funkcji
        print(text)

    @staticmethod
    def input_text(entry):  # Wzięcie string i return
        text = input(str(entry))
        return text

    @staticmethod
    def input_number(stri, rang):  # Czy jest to liczba w  liście
        entry = input(stri)
        while True:
            if Console.is_int(entry):
                numer = int(entry)
                is_in_range = False
                for x in rang:
                    if x == numer:
                        is_in_range = True
                if is_in_range:
                    return numer
                else:
                    a = ['Ten numer nie nalerzy do listy. Podaj numer należący do listy: ', str(rang)]
                    a = ''.join(a)
                    entry = input(a)

            else:
                a = ['To nie jest numer. Podaj numer należący do listy: ', str(rang)]
                a = ''.join(a)
                entry = input(a)

    @staticmethod
    def input_numer_in_range(stri, beginr, endr):  # czy jest to liczba pomiędzy tymi
        entry = input(stri)
        while True:
            if Console.is_int(entry):
                numer = int(entry)
                if beginr <= numer <= endr:
                    return numer
                else:
                    a = ['Ten numer nie nalerzy do zakresu. Podaj całkowity numer w zakresie: ', str(beginr), ' do ',
                         str(endr)]
                    a = ''.join(a)
                    entry = input(a)
            else:
                a = ['To nie jest numer. Podaj całkowity numer w zakresie: ', str(beginr), ' do ', str(endr)]
                a = ''.join(a)
                entry = input(a)

    @staticmethod
    def input_yes_or_no(stri):  # tak czy nie
        a = stri + ', odpowiedz T na tak lub N na nie'
        entry = input(a)
        while True:
            if entry == 't' or entry == 'T':
                return True
            if entry == 'n' or entry == 'N':
                return False
            entry = input('T na tak lub N na nie')

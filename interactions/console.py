import os
class Console:

    def clear_view(): # czyszczenie ekranu TYLKO NA LINUXS!!!
        os.system('clear')

    def output (text): # Print w funkcji
        print(text)

    def input_text (entry): # Zamiana na string i return
        text = str(entry)
        return text

    def input_number (stri,rang): # czy jest to liczba w  liście
        try:
            numer = int(stri)
            is_in_range = False
            for x in rang:
              if x == numer:
                    is_in_range = True
            if is_in_range == True:
                return numer
            else:
                a = ['Podaj całkowity numer należący do listy: ', str(rang)]
                a = ''.join(a)
                newn = input(a)
                Console.input_number(newn, rang)
        except ValueError:
            a = ['Podaj całkowity numer należący do listy: ',str(rang) ]
            a = ''.join(a)
            newn = input(a)
            Console.input_number(newn, rang)

    def input_numer_in_range (stri,beginr,endr): #czy jest to liczba pomiędzy tymi
        try:
            numer = int(stri)
            is_in_range = False
            for x in range(beginr, endr + 1):  # pomiędzy łacznie z liczbą końcową
                if x == numer:
                    is_in_range = True
            if is_in_range == True:
                return numer
            else:
                a = ['Podaj całkowity numer w zakresie: ', str(beginr), ' do ', str(endr)]
                a = ''.join(a)
                newn = input(a)
                return Console.input_numer_in_range(newn,beginr,endr)
        except ValueError:
            a = ['Podaj całkowity numer w zakresie: ',str(beginr),  ' do ',str(endr)]
            a = ''.join(a)
            newn = input(a)
            return Console.input_numer_in_range(newn, beginr, endr)

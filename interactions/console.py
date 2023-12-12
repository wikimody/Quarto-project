class Console:
    def clear_view(): # czyszczenie ekranu TYLKO NA LINUXS!!!
        import os
        os.system('clear')

    def output (text): # Print w funkcji
        print(text)

    def input_text (wejscie): # Zamiana na string i return
        text = str(wejscie)
        return text

    def input_number (stri,rang): # czy jest to liczba w  liście
        try:
            numer = int(stri)
            czy_w_range = False
            for x in rang:
              if x == numer:
                    czy_w_range = True
            if czy_w_range == True:
                return numer
            else:
                return False
        except ValueError:
            return False

    def input_numer_in_range (stri,beginr,endr): #czy jest to liczba pomiędzy tymi
        try:
            numer = int(stri)
            czy_w_range = False
            for x in range(beginr, endr + 1):  # pomiędzy łacznie z liczbą końcową
                if x == numer:
                    czy_w_range = True
            if czy_w_range == True:
                return numer
            else:
                return False
        except ValueError:
            return False




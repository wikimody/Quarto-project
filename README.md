# Projekt Quarto (PWI)

Projekt zespołowy gry wykonany na potrzeby zajęć *Podstawowego Warsztatu Informatyka*.

## Cel projektu

Zadaniem zespołu było zaimplementowanie gry Quarto oraz napisanie botów, które mogłyby również
grać w grę.

## Zasady gry

Obowiązują wszystkie podstawowe zasady gry oprócz potrzeby wołania *Quarto*
(gra kończy się automatycznie, gdy zostanie spełniony warunek zwycięstwa). \
Pełny zbiór zasad:
https://www.ultraboardgames.com/quarto/game-rules.php

## Wymagania systemowe

- Gra w założeniu jest przeznaczona do użytku w systmie Linux.
- Do uruchomienia gry potrzebny jest interpeter języka Python (Wesja: 3.10.12 jest działająca).
- Gra posiada już skompilowane boty. 
Jeśli użytkownik sam chce je skompilować potrzebuje do tego kompilatora języka C++ (autor tych słów używał g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0).

Instalacja pythona wg: https://www.python.org/
Instalacja kompilatora CPP: wykonać w terminalu polecenie:

> sudo apt update && sudo apt install build-essential

Aby odpowiednio skompilować bota należy wykonać odpowiednią komendę:

> g++ -o {nazwa_skompilowanego pliku} {ścieżka_do_pliku_cpp}

Następnie skompilowany plik należy umieścić w folderze cpp_bots/bin/.

## Uruchamianie gry

Uruchomienie gry polega na wywołaniu skryptu *main.py* znajdującego się w głównym katalogu gry.
Dokonujemy tego w klasyczny sposób (powinniśmy znajdować się w katalogu z main.py):

> python main.py

## Podstawowe funkcjonalności

Program umożliwia 4 tryby gry:

1. Gra człowieka z człowiekiem (lokalnie, w trybie "hot seat")
2. Gra człowieka z człowiekiem (sieciowo)
3. Gra człowieka z botem
4. Starcie botów

Niezależnie od trybu gry, program za każdym razem wyświetla stan planszy w konsoli. W zależoności
od rodzaju ruchu (wybieranie pionka, położenie pionka) gracz na konsoli otrzymuje odpowiednie informacje (dostępne pionki, stan planszy).

W trybie 3. oraz 4. użytkownik ma możliwość wyboru między 3 botami.

## Współautorzy

Klara Nowaczyk 346456 \
Agata Rajczakowska 345398 \
Mikołaj Dygoń 346656 \
Tatiana Mikshta 344451 \
Wiktor Modrzewski 346200 \
Yurii Pryimak 343898 \
Daniel Boguszewski 315942 \
Krzysztof Piekarczyk 324527

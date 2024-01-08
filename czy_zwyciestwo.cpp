// Program do sprawdzania, czy na planszy jest ulozenie wygrywajace
//zwraca 1, gdy gdy ktos juz wygral
//zwraca 0 wpp

#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

// funkcje zamieniajace liczbe z systemy 16 na 10 i z 10 na 2
int HexToDec (char hex);
string DecToBin (int dec);


int main( int argc, char *argv[])
{
    //sprawdzanie poprawnosci wejscia
    if (argc != 2){
        fprintf (stderr, "Zla liczba argumrntow\n");
        return 1;
    }
    if (strlen (argv[1]) != 16){
        fprintf (stderr, "Podaj sam opis planszy czyli 16 znakow\n");
        return 2;
    }

    //plansza - dwuwymiarowa tablica stringow (albo jak kto woli 3-wymiarowa tablica charow) do przechowywania stanu planszy, gdzie pionki sa w zapisie binarnym jako ciagi 4 znakow
    string plansza[4][4];
    for (int i=0; i<16; i++){
        if (argv[1][i] == 'p')
            plansza[i/16][i%16] = "pppp";
        else
            plansza[i/16][i%16] = DecToBin( HexToDec(argv[1][i]) );
    }

    /*wypis kontrolny planszy jakby ktos chcial testowac
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++)
            cout <<plansza[i][j]<<" ";
        cout << endl;
    }
    cout << endl;
    */

    //sprawdzanie zwyciestwa
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            // sprawdzanie poziomo czy jest zwyciestwo (sprawdzenie, czy wszystkie pionki w danym rzedzie maja taki sam j'oty bit)
            if (plansza[i][0][j] != 'p')
                if ( (plansza[i][0][j] == plansza[i][1][j]) && (plansza[i][0][j] == plansza[i][2][j]) && (plansza[i][0][j] == plansza[i][3][j])  ){
                    cout << 1;
                    return 0;
                }

            //sprawdzanie pionowo czy jest zwyciestwo (podobnie tylko dla kolumn)
            if (plansza[0][i][j] != 'p')
                if ( (plansza[0][i][j] == plansza[1][i][j]) && (plansza[0][i][j] == plansza[2][i][j]) && (plansza[0][i][j] == plansza[3][i][j]) ){
                    cout << 1;
                    return 0;
                }
        }
        //sprawdzanie przekatnych
        if (plansza[0][0][i] != 'p')
            if ( (plansza[0][0][i] == plansza[1][1][i]) && (plansza[0][0][i] == plansza[2][2][i]) && (plansza[0][0][i] == plansza[3][3][i]) ) {
                cout << 1;
                return 0;
            }
        if (plansza[0][3][i] != 'p')
            if ( (plansza[0][3][i] == plansza[1][2][i]) && (plansza[0][3][i] == plansza[2][1][i]) && (plansza[0][3][i] == plansza[3][0][i]) ){
                cout << 1;
                return 0;
            }
    }
    cout << 0;

    return 0;
}
int HexToDec (char hex)
{
    if (hex >= '0' && hex <= '9')
        return hex - '0';
    else return hex - 'A' + 10;

}
string DecToBin (int dec)
{
    string bin = "0000";
    for (int i=3; i>=0; i--){
        if (dec%2)
            bin[i] = '1';
        dec /= 2;
    }
    return bin;
}

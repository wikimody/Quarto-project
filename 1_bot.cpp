//1. bot
#include <iostream>
#include <ctime>
#include <string>

using namespace std;

// funkcja sprawdzająca wykorzystanie pionka wcześniej
int spr_wykorzystania(char postawione[17], int pionek, char pionki[16])
{
    for(int i = 0; i < 17; i++)
    {
        if(pionki[pionek] == postawione[i]) return 0;
    }
    return 1;
}

int main(int argc, char *argv[])
{
    char plansza[4][4], postawione[17];
    char pionki[16] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    int licznik = 0;
    for(int i = 1; i < 16; i++)
        postawione[i] = '-1';

    // "Wizualizujemy" planszę w tablicy: plansza. Zapisujemy, które figury zostały już wykorzzystane.
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
        {
            plansza[i][j] = argv[1][licznik];
            if(argv[1][licznik] != 'p')
                postawione[licznik] = argv[1][licznik];
            licznik++;
        }
    postawione[licznik] = argv[1][licznik];
    srand(time(NULL));
    int wiersz, kolumna, pionek;
    do
    {
        wiersz = rand() % 4;
        kolumna = rand() % 4;
    } while(plansza[wiersz][kolumna] != 'p');

    pionek = 16;
    for(int i = 0; i < 16; i++)
    {
        if(spr_wykorzystania(postawione, i, pionki) == 1)
        {
            pionek = i;
            break;
        }
    }

    cout << wiersz+1 << kolumna+1 << pionki[pionek] << "\n";
    return 0;
}

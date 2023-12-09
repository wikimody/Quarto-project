//1. bot
#include <iostream>
#include <ctime>
#include <string>

using namespace std;

// funkcja sprawdzaj¹ca wykorzystanie pionka wczeœniej
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

    // "Wizualizujemy" planszê w tablicy: plansza. Zapisujemy, które figury zosta³y ju¿ wykorzzystane.
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
    } while(plansza[wiersz][kolumna] == 'p');

    do{
        pionek = rand()%16;
    } while(spr_wykorzystania(postawione,pionek, pionki) == 0);


    cout << wiersz << kolumna << pionki[pionek] << "\n";
    return 0;
}

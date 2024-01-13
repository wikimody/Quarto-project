//2. bot
#include <iostream>
#include <ctime>
#include <string>

using namespace std;

// funkcja sprawdzajaca wykorzystanie pionka wczesniej
int spr_wykorzystania(char postawione[17], int pionek, char pionki[16])
{
    for(int i = 0; i < 17; i++)
    {
        if(pionki[pionek] == postawione[i]) return 0;
    }
    return 1;
}

int zamiana_pionkow(char pionek)
{
	if(pionek >= '0' && pionek <= '9') pionek -= '0';
	else if(pionek >= 'A' && pionek <= 'F')pionek -= 'A' - 10;
	//jesli dostalismy pionek spoza przedzialu zwracamy po prostu 1 0 0 0 0, czyli 16 (obsluga bledu, mozna zmienic)
	else return 16;

	return (int)pionek;
}


int main(int argc, char *argv[])
{
    int plansza[4][4], postawione[17], pionki[16];
    int licznik = 0;
    for(int i = 0; i < 16; i++)
    {
        postawione[i] = 16;
        pionki[i] = i;
    }

    // "Wizualizujemy" plansze w tablicy: plansza. Zapisujemy, które figury zostaly juz wykorzystane.
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            plansza[i][j] = zamiana_pionkow(argv[1][licznik]);
            cout << plansza[i][j];
            if(argv[1][licznik] != 'p')
                postawione[licznik] = zamiana_pionkow(argv[1][licznik]);
            licznik++;
        }
        cout << endl;
    }
    postawione[licznik] = argv[1][licznik]; // pionek ktory dostalismy????????


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

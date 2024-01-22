//2. bot
#include <iostream>
#include <string.h>
#include <stdio.h>
#include<ctime>
#include <string>
#include <cstdlib>
using namespace std;

// funkcja sprawdzajaca wykorzystanie pionka wczesniej
bool spr_wykorzystania(int postawione[17], int pionek)
{
    for(int i = 0; i < 17; i++)
    {
        if(pionek == postawione[i]) return 0;
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

bool czy_istnieje_cecha(int p[4]) //zwraca 0 lub 1 w zaleznosci od tego czy istnieje cecha wspolna
{
	//cout<<"Funkcja wywolana"<<endl;
	for(int i = 0; i < 4; i++)
        if(p[i] > 16 || p[i] < 0)
            return 0;//sprawdzenie poprawnosci argumentow


	short int zapis = (1 << 4)-1 , znegacja = zapis; //short ma 4 bajty, zapisy na poczatku musza byc ustawione na '1111'
	for(int i = 0; i < 4; i++)
	{
		if(p[i] != 16)//jesli pole niepuste
		{
			zapis &= p[i]; //sprawdzenie dla 1
			znegacja &= ~(p[i]); //sprawdzenie dla 0
		}

	}

	if((zapis & (1 << 4)-1) != 0 || (znegacja & (1 << 4)-1) != 0) //- wiaze mocniej niz & wiec kolejnosc bedzie poprawna
	{
		return 1;
	}
	return 0;
}

int znajdz_pole_przeciwnika (int plansza[4][4], int postawione[17])
{
    int pionki_do_sprawdzenia_w[4] = {16, 16, 16, 16}, pionki_do_sprawdzenia_k[4] = {16, 16, 16, 16}, pionki_do_sprawdzenia_p_lg[4] = {16, 16, 16, 16}, pionki_do_sprawdzenia_p_ld[4] = {16, 16, 16, 16};
    int ilosc_pionkow_w = 0, ilosc_pionkow_k = 0, ilosc_pionkow_p_lg = 0, ilosc_pionkow_p_ld = 0;
    bool czy_wygrana = 0;


    //sprawdzenie w wierszy
    for(int i = 0; i < 4; i++)
    {
        ilosc_pionkow_w = 0;
        ilosc_pionkow_k = 0;
        for(int j = 0; j < 4; j++)//przepisywanie pionkow w wierszu, jesli wystepuja
        {
            if(plansza[i][j] != 16)
            {
                pionki_do_sprawdzenia_w[ilosc_pionkow_w] = plansza[i][j];
                //cout << pionki_do_sprawdzenia_w[ilosc_pionkow_w] << " ";
                ilosc_pionkow_w++;
            }

            if(plansza[j][i] != 16)
            {
                pionki_do_sprawdzenia_k[ilosc_pionkow_k] = plansza[j][i];
                //cout << pionki_do_sprawdzenia_k[ilosc_pionkow_k] << " ";
                ilosc_pionkow_k++;
            }
        }
        //cout <<  endl;

        if(plansza[i][i] != 16)
        {
            pionki_do_sprawdzenia_p_lg[ilosc_pionkow_p_lg] = plansza[i][i];
            //cout << pionki_do_sprawdzenia[ilosc_pionkow] << " ";
            ilosc_pionkow_p_lg++;
        }

        if(plansza[3 - i][i] != 16)
        {
            pionki_do_sprawdzenia_p_ld[ilosc_pionkow_p_ld] = plansza[3 - i][i];
            // cout << pionki_do_sprawdzenia[ilosc_pionkow] << " ";
            ilosc_pionkow_p_ld++;
        }

        if(ilosc_pionkow_w == 3) //sprawdzamy czy mozemy dostawic czwarty pionek by wygrac
        {
            pionki_do_sprawdzenia_w[ilosc_pionkow_w] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_w) == 1)
            {
                czy_wygrana = 1;
                break;
            }
        }

        if(ilosc_pionkow_k == 3) //sprawdzamy czy mozemy dostawic czwarty pionek by wygrac
        {
            pionki_do_sprawdzenia_k[ilosc_pionkow_k] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_k) == 1)
            {
                czy_wygrana = 1;
                break;
            }
        }

        for(int j = 0; j < 4; j++){
            pionki_do_sprawdzenia_w[j] = 16;
            pionki_do_sprawdzenia_k[j] = 16;
        }
    }
    if (!czy_wygrana){
        if(ilosc_pionkow_p_lg == 3) //sprawdzamy czy mozemy dostawic czwarty pionek by wygrac
        {
            pionki_do_sprawdzenia_p_lg[ilosc_pionkow_p_lg] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_p_lg) == 1)
                czy_wygrana = 1;
        }
    }

    if (!czy_wygrana){
        if(ilosc_pionkow_p_ld == 3) //sprawdzamy czy mozemy dostawic czwarty pionek by wygrac
        {
            pionki_do_sprawdzenia_p_ld[ilosc_pionkow_p_ld] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_p_ld) == 1)
                czy_wygrana = 1;
        }
    }
    return czy_wygrana;
}

int main(int argc, char *argv[])
{
    //sprawdzanie poprawnosci wejscia
    if (argc != 2){
        fprintf (stderr, "Zla liczba argumentow\n");
        return 1;
    }
    if (strlen (argv[1]) != 17){
        fprintf (stderr, "Podaj sam opis planszy czyli 16 znakow\n");
        return 2;
    }

    int plansza[4][4], postawione[17], pionki[16]; //postawione[0.. 15] - uzyte pionki, postawione[16] - pionek do postawienia
    int licznik = 0, przegrana[4][4];   //przegrana[cos][cos] = -1 gdy postawnienie tam pionka oznacza ustawienie 3 takich samych cech w lini
    for(int i = 0; i < 16; i++)
    {
        postawione[i] = 16;
        pionki[i] = i;
    }

    // "Wizualizujemy" plansze w tablicy: plansza. Zapisujemy, ktĂłre figury zostaly juz wykorzystane.
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            plansza[i][j] = zamiana_pionkow(argv[1][licznik]);
            //cout << plansza[i][j] << " ";
            if(argv[1][licznik] != 'p')
                postawione[licznik] = zamiana_pionkow(argv[1][licznik]);
            licznik++;

            przegrana[i][j] = 0;
        }
        //cout << endl;
    }
    postawione[licznik] = zamiana_pionkow(argv[1][licznik]); // pionek ktory dostalismy

    //sufiksy: _w - w wierszu, _k - w kolumnie, _p_lg - przekatna od lewego gornego rogu (hehe plg), _p_ld - przekatna od lewego dolnego rogu
    int pionki_do_sprawdzenia_w[4] = {16, 16, 16, 16}, pionki_do_sprawdzenia_k[4] = {16, 16, 16, 16}, pionki_do_sprawdzenia_p_lg[4] = {16, 16, 16, 16}, pionki_do_sprawdzenia_p_ld[4] = {16, 16, 16, 16};
    int ilosc_pionkow_w = 0, ilosc_pionkow_k = 0, ilosc_pionkow_p_lg = 0, ilosc_pionkow_p_ld = 0;
    int wygrana_x_w = -1, wygrana_y_w = -1,  wygrana_x_k = -1, wygrana_y_k = -1, wygrana_x_p_lg = -1, wygrana_y_p_lg = -1, wygrana_x_p_ld = -1, wygrana_y_p_ld = -1;
    int win_x = -1, win_y = -1;
    bool czy_wygrana = 0;
	//R - random, wersja dla bota 50/50
	srand(time(NULL));
    int wierszR, kolumnaR, pionekR, los;
    los = rand()%2;
    cout<<"losowanie1"<<endl;
    if(los)
	{
		cout<<"weszlo"<<endl;
  	  do
 	   {
 	   	cout<<"losowanie2"<<endl;
 	       wierszR = rand() % 4;
  	      	kolumnaR = rand() % 4;
  	  } while(plansza[wierszR][kolumnaR] != 16);
	
   	 pionekR = 16;
   	 for(int i = 0; i < 16; i++) //ta wersja wrzuca pierwszego dostapnego pionka przeciwnikowi
  	  {
  	      if(spr_wykorzystania(postawione, i) == 1)
 	       {
 	       	cout<<"pionek"<<endl;
 	           pionekR = i;
 	           break;
 	       }
 	   }
	
  	  cout << wierszR+1 << kolumnaR+1 << pionki[pionekR] << "\n";
    	return 0;
	} 
	
    for(int i = 0; i < 4; i++)
    {
        ilosc_pionkow_w = 0;
        ilosc_pionkow_k = 0;
        for(int j = 0; j < 4; j++)//przepisywanie pionkow w wierszu, jesli wystepuja
        {
            //przepisywanie pionkow z wiersza
            if(plansza[i][j] != 16)
            {
                pionki_do_sprawdzenia_w[ilosc_pionkow_w] = plansza[i][j];
                //cout << pionki_do_sprawdzenia_w[ilosc_pionkow_w] << " ";
                ilosc_pionkow_w++;
            }
            else // gdy puste pole to mamy potencjalne pole do wygranej
            {
                wygrana_x_w = i;
                wygrana_y_w = j;
            }
            //przepisywanie pionkow z kolumny
            if(plansza[j][i] != 16)
            {
                pionki_do_sprawdzenia_k[ilosc_pionkow_k] = plansza[j][i];
                //cout << pionki_do_sprawdzenia_k[ilosc_pionkow_k] << " ";
                ilosc_pionkow_k++;
            }
            else // gdy puste pole to mamy potencjalne pole do wygranej
            {
                wygrana_x_k = j;
                wygrana_y_k = i;
            }

        }
        //cout <<  endl;

        //przepisywanie z jednej przekatnej
        if(plansza[i][i] != 16)
        {
            pionki_do_sprawdzenia_p_lg[ilosc_pionkow_p_lg] = plansza[i][i];
            //cout << pionki_do_sprawdzenia[ilosc_pionkow] << " ";
            ilosc_pionkow_p_lg++;
        }
        else // gdy puste pole to mamy potencjalne pole do wygranej
        {
            wygrana_x_p_lg = i;
            wygrana_y_p_lg = i;
        }

        //przepisywanie z drugiej przekatnej
        if(plansza[3 - i][i] != 16)
        {
            pionki_do_sprawdzenia_p_ld[ilosc_pionkow_p_ld] = plansza[3 - i][i];
            // cout << pionki_do_sprawdzenia[ilosc_pionkow] << " ";
            ilosc_pionkow_p_ld++;
        }
        else // gdy puste pole to mamy potencjalne pole do wygranej
        {
            wygrana_x_p_ld = 3 - i;
            wygrana_y_p_ld = i;
        }


        // sprawdzenie czy mozemy dostawic pionek w wierszu zeby wygrac
        if(ilosc_pionkow_w == 3)
        {
            pionki_do_sprawdzenia_w[ilosc_pionkow_w] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_w) == 1)
            {
                win_x = wygrana_x_w;
                win_y = wygrana_y_w;
                czy_wygrana = 1;
                break;
            }
            //cout << "Wygrane x, y: " << wygrana_x << ", " << wygrana_y << endl;
            wygrana_x_w = -1, wygrana_y_w = -1;
        }
        //sprawdzamy czy jesli dostawimy trzeci w rzedzie pionek to przeciwnik bedzie mogl wygrac
        else if (ilosc_pionkow_w == 2)
        {
            pionki_do_sprawdzenia_w[ilosc_pionkow_w] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_w) == 1)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(plansza[i][j] == 16)
                        przegrana[i][j] = -1;
                }
            }
        }
        // sprawdzenie czy mozemy dostawic pionek w kolumnie zeby wygrac
        if(ilosc_pionkow_k == 3)
        {
            pionki_do_sprawdzenia_k[ilosc_pionkow_k] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_k) == 1)
            {
                win_x = wygrana_x_k;
                win_y = wygrana_y_k;
                czy_wygrana = 1;
                break;
            }
            //cout << "Wygrane x, y: " << wygrana_x << ", " << wygrana_y << endl;
            wygrana_x_k = -1, wygrana_y_k = -1;
        }
        //sprawdzamy czy jesli dostawimy trzeci w kolumnie pionek to przeciwnik bedzie mogl wygrac
        else if (ilosc_pionkow_k == 2)
        {
            pionki_do_sprawdzenia_k[ilosc_pionkow_k] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_k) == 1)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(plansza[j][i] == 16)
                        przegrana[j][i] = -1;
                }
            }
        }

        for(int j = 0; j < 4; j++){
            pionki_do_sprawdzenia_w[j] = 16;
            pionki_do_sprawdzenia_k[j] = 16;
        }
    }
    //jak nie to sprawdzamy czy mozna dostawic w przekatnych
    if (!czy_wygrana){
        if(ilosc_pionkow_p_lg == 3)
        {
            pionki_do_sprawdzenia_p_lg[ilosc_pionkow_p_lg] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_p_lg) == 1)
            {
                win_x = wygrana_x_p_lg;
                win_y = wygrana_y_p_lg;
                czy_wygrana = 1;
            }
            //cout << "Wygrane x, y: " << wygrana_x << ", " << wygrana_y << endl;
            //wygrana_x_p_lg = -1, wygrana_y_p_lg = -1;
        }
        else if (ilosc_pionkow_p_lg == 2)
        {
            pionki_do_sprawdzenia_p_lg[ilosc_pionkow_p_lg] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_p_lg) == 1)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(plansza[j][j] == 16)
                        przegrana[j][j] = -1;
                }
            }
        }
    }

    //i tu druga przekatna
    if (!czy_wygrana){
        if(ilosc_pionkow_p_ld == 3)
        {
            pionki_do_sprawdzenia_p_ld[ilosc_pionkow_p_ld] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_p_ld) == 1)
            {
                win_x = wygrana_x_p_ld;
                win_y = wygrana_y_p_ld;
                czy_wygrana = 1;
            }
            //cout << "Wygrane x, y: " << wygrana_x << ", " << wygrana_y << endl;
            //wygrana_x_p_ld = -1, wygrana_y_p_ld = -1;
        }
        else if (ilosc_pionkow_p_ld == 2) //sprawdzamy czy jesli dostawimy trzeci pionek to przeciwnik bedzie mogl wygrac
        {
            pionki_do_sprawdzenia_p_ld[ilosc_pionkow_p_ld] = postawione[16];
            if(czy_istnieje_cecha(pionki_do_sprawdzenia_p_ld) == 1)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(plansza[3 - j][j] == 16)
                        przegrana[3 - j][j] = -1;
                }
            }
        }
    }
    //jesli nie ma pola do wygranej, zwracamy pole gdzie nie dostawimy trzeciego o takiej samej cesze
    if(!czy_wygrana)
    {
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                if(plansza[i][j] == 16 && przegrana[i][j] != -1)
                {
                    win_x = i;
                    win_y = j;
                    czy_wygrana = 1;
                    break;
                }
            }
            if(czy_wygrana)
                break;
        }
        //gdy nie mamy takiego pola wypisujemy pierwsze puste pole
        if(!czy_wygrana){
            for(int i = 0; i < 4; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(plansza[i][j] == 16)
                    {
                        win_x = i;
                        win_y = j;
                        czy_wygrana = 1;
                        break;
                    }
                }
                if(czy_wygrana)
                    break;
            }
        }
    }
    if (!czy_wygrana){
        cout<< "PELNA PLANSZA UGH";
        return 2137;
    }
    //          *****           WYPIS WSPOLRZEDNYCH         *****
    else {
        //wstawienie pionka do planszy zeby wylosowac dobry pionek dla oponenta
        plansza[win_x][win_y] = postawione[16];
    }

    int pionek = 16;
    for(int i = 0; i < 16; i++)//wybieranie pionka dla przeciwnika
    {
        if(spr_wykorzystania(postawione, pionki[i]) == 1)
        {
            postawione[16] = pionki[i];
            if (znajdz_pole_przeciwnika (plansza, postawione) == 0){
                pionek = pionki[i];
                break;
            }
        }
    }
    // jesli pionek == 16 to wybieramy pierwszego dostepnego i przegrywamy
    if (pionek == 16){
        for (int i=0; i<16; i++)
            if(spr_wykorzystania(postawione, pionki[i]) == 1){
                pionek = pionki[i];
                break;
            }
    }

    char pionki_char[16] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};

    if(pionek != 16)
        cout<<win_x+1<<win_y+1<< pionki_char[pionek] << endl;
    else cout<<win_x+1<<win_y+1<< pionek << endl;

    return 0;
}

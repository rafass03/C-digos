//Lista 2 do JUDE
//Questão 6

#include <iostream>
using namespace std;

int main() 
{
int P, S, A, D, ValorA, ValorD, Contador1, Contador2;
cin >> P;
cin >> S;
ValorA = 0;
ValorD = 0;
Contador1 = 0;
Contador2 = 0;

    while (Contador2 < P)
        { 
            while (Contador1 < S)
            {
            cin >> A >> D;
            ValorA = ValorA + A;
            ValorD = ValorD + D;
            Contador1 = Contador1 + 1;
            }
            cout << ValorA << " " << ValorD << endl;
            Contador2 = Contador2 + 1;
            ValorA = 0;
            ValorD = 0;
            Contador1 = 0;
        }
return 0;
}
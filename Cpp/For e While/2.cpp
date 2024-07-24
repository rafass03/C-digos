//Lista 2 do JUDE
//Questão 2

#include <iostream>
using namespace std;

int main() 
{
int N, P, Contador, Valor;
cin >> N;
Contador = 0;
Valor = 0;

    while (Contador < N)
        { 
        cin >> P;
            if (P > Valor)
            {
                Valor = P;
            }
        Contador = Contador + 1;
        }
cout << Valor << endl;
return 0;
}
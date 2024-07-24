//Lista 2 do JUDE
//Questão 3

#include <iostream>
using namespace std;

int main() 
{
int T, P, Valor;
cin >> T;
Valor = 0;

    while (P != 0)
        { 
        cin >> P;
        if (P > Valor)
            {
                Valor = P;
            }
        }

if (Valor > T)
{
cout << "ALARME" << endl;
}
else
{
cout << "O Havai pode dormir tranquilo" << endl;
}
return 0;
}
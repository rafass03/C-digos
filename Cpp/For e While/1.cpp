//Lista 2 do JUDE
//Questão 1

#include <iostream>
using namespace std;

int main() 
{
int N, P, W, Contador;
cin >> N;
Contador = 0;

    while (Contador < N)
        { 
        cin >> P >> W;
        cout << P+W << endl;
        Contador = Contador + 1;
        }
return 0;
}
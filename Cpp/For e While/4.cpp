//Lista 2 do JUDE
//Questão 4

#include <iostream>
using namespace std;

int main() 
{
int N, Valor;
cin >> N;
Valor = N;

while (Valor % 2 == 0)
{
Valor = Valor/2;
}

if (Valor == 1)
{
    cout << "Dattebayo" << endl;
}
else
{
    cout << "Tururuuu" << endl;
}
return 0;
}
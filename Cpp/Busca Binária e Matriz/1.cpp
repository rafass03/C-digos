//Lista 4 do JUDE
//Questão 1

#include <iostream>
using namespace std;

int main()
{
  int N, XA, menor_i, aux;
  cin >> N;
  int VA[N];

  for (int i = 0; i < N; i++)
  {
    cin >> XA;
    VA[i] = XA;
  }

  for(int j = 0; j < N-1; j++)
  {
    menor_i = j;
    for(int i = j+1; i < N; i++)
    {
      if(VA[i] < VA[menor_i])
      menor_i = i;
    }
    aux = VA[j];
    VA[j] = VA[menor_i];
    VA[menor_i] = aux;
 }

 for (int i = 0; i < 8; i++)
 { 
    cout << VA[i] << " ";
 }
  return 0;
}

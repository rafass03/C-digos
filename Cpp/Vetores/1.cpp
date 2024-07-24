//Lista 3 do JUDE
//Questão 1

#include <iostream>
using namespace std;

int main()
{
  int N, S, Altura, count;
  cin >> N;
  int Obstaculos [N];
  count=0;

    for (int i = 0; i < N; i++)
    {
      cin >> Altura;
      Obstaculos [i] = Altura;
    }
cin >> S;
    for (int i = 0; i < N; i++)
      {
        if(Obstaculos [i] <= S)
        {
          count += 1;
        }
        else
        {
          break;
        }
      }
cout << count << endl;
  if (count == N)
  {
    cout << "1" << endl;
  }
  else
  {
    cout << "0" << endl;
  }
return 0;
}
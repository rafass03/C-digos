//Lista 2 do JUDE
//Questão 5

#include <iostream>
using namespace std;

int main()
{
  int P;
  cin >> P;
  int Altura;
  Altura = P;

    while (P > 0)
    {
      for (int S = P-1; S > 0; S--)
      {
        cout << '>';
      }

      for (int H = 0; H <= (Altura-P); H++)
      {
        cout << '#';
      }

    P--;
    cout << "\n";

    }  
  return 0;
}
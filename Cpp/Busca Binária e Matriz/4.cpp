//Lista 4 do JUDE
//Questão 4

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
  int N, M, C, i;

  cin >> N;
  vector <string> VA(N);
  for (i = 0; i < N; i++)
  {
    cin >> VA[i];
  }

  cin >> M;
  vector <string> VB(M);
  for (i = 0; i < M; i++)
  {
    cin >> VB[i];
  }

  cin >> C;
  vector <string> VC(C);
  for (i = 0; i < C; i++)
  {
    cin >> VC[i];
  }

  for (i = 0; i < C; i++)
  {
    if (binary_search(VA.begin(), VA.end(), VC[i]))
    {
      cout << "Geral" << endl;
    }
    else
    {
      cout << "Proibido" << endl;
    }
  }
  return 0;
}

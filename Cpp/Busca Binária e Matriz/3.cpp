//Lista 4 do JUDE
//Questão 3

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int N, i, Q, j;
  
  cin >> N;
  vector <string> VA(N);
  for (i = 0; i < N; i++)
  {
    cin >> VA[i];
  }

  cin >> Q;
  vector <string> VB(Q);
  for (i = 0; i < Q; i++)
  {
    cin >> VB[i];
  }

  for (i = 0; i < Q; i++)
  {
    if (binary_search(VA.begin(), VA.end(), VB[i]))
      {
        cout << VB[i] << " vive!" << endl;
      }
      else
      {
        cout << VB[i] << " foi extinto :(" << endl;
      }
  }
  return 0;
}
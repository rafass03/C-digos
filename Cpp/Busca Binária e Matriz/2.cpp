//Lista 4 do JUDE
//Questão 2

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  int N, i;
  cin >> N;
  cin.ignore();
  vector <string> VA(N);

  for (i = 0; i < N; i++)
  {
    getline(cin, VA[i]);
  }

  sort(VA.begin(), VA.end());

  for (i = 0; i < N; i++)
  {
    cout << VA[i] << endl;
  }
  return 0;
}

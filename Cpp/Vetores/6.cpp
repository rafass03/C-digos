//Lista 3 do JUDE
//Questão 6

#include <iostream>
using namespace std;

int main() 
{
  int N, C, X;
  cin >> N;
  int V[N];
  
  for (int i = 0; i < N; i++)
  {
  	cin >> X;
  	V[i] = X;
  }
  
  cin >> C;
  
  for (int i = 0; i < N; i++)
  {
  	if (V[i] == C)
  		{
  		cout << C << endl;
  		break;
  		}
  	if (i == (N-1))
  		{
  		cout << "-1" << endl;
  		}
  }
  return 0;
}

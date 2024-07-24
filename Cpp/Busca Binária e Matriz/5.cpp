//Lista 4 do JUDE
//Questão 5

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int main() 
{
  int i, j, M, N, P, count;
  cin >> M >> N;
  int T[M][N];
  count = 0;
  
  for (i = 0; i < M; i++)
  	{
  		for (j = 0; j < N; j++)
  			{
  				cin >>T[i][j];
  			}
  	}
  
  cin >> P;
  
  for (i = 0; i < M; i++)
  	{
  		for (j = 0; j < N; j++)
  			{
  				if (T[i][j] == P)
  					{
  						count += 1;
  					}
  			}			
  	}
  
  cout << "Ash pegou " << count << " pokemon" << endl;
  
  return 0;
}

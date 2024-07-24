//Lista 4 do JUDE
//Questão 8

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int main() 
{
	int i, j, N, M, L, C, count=0;
	cin >> N >> M;
	int T[N][N];
  
	for (i=0; i<N; i++)
	{
  		for (j=0; j<N; j++)
  		{
  			cin >> T[i][j];
  		}
  	}
  
  	for (i=0; i<M; i++)
	{
		cin >> L >> C;
		for (j=L-1; j>=0; j--)
		{
			if (T[j][C] == 1)
			{
				count++;
				T[j][C] = 0;
				break;
			}
		}
	}

	cout << count << endl;
  	return 0;
}

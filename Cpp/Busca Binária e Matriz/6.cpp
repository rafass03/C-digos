//Lista 4 do JUDE
//Questão 6

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int main() 
{
	int i, j, X, Y, N, Harry=0, Ron=0;
	cin >> N;
	int T[N][N];
  
	for (i=0; i<N; i++)
	{
  		for (j=0; j<N; j++)
  		{
  			cin >> T[i][j];
  		}
  	}
  
  	cin >> X >> Y;
  
  	for (i=0; i<N; i++)
  	{
		Harry += T[X][i];
  	}
  	for (j=0; j<N; j++)
  	{
  		Ron += T[j][Y];
  	}
	
	if (Y >= X)
	{
		Harry -= T[X][Y];
	}
	else
	{
		Ron -= T[X][Y];
	}

  	cout << "Harry " << Harry << endl;
	cout << "Ron " << Ron << endl;
  
  	return 0;
}

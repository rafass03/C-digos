//Lista 4 do JUDE
//Questão 7

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int main() 
{
	int i, j, X, Y, count=0;
	int T[8][8];
  
	for (i=0; i<8; i++)
	{
  		for (j=0; j<8; j++)
  		{
  			cin >> T[i][j];
  		}
  	}
  
  	cin >> X >> Y;
  
  	for (i=0; i<8; i++)
	{
  		if (T[X][i] == 2)
			{
				count++;
				break;
			}
  	}

	for (i=0; i<8; i++)
	{
  		if (T[i][Y] == 2)
			{
				count++;
				break;
			}
  	}

	cout << count << endl;
  	return 0;
}

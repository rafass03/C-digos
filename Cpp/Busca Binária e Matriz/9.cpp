//Lista 4 do JUDE
//Questão 9

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() 
{
	int i, j;
	string T[10][10];
  
	for (i=0; i<10; i++)
	{
  		for (j=0; j<10; j++)
  		{
  			cin >> T[i][j];
  		}
  	}
  
  	for (i=0; i<10; i++)
	{
		for (j=0; j<10; j++)
		{
			if ((T[i][j] == "t") &&
			((i>0 && T[i-1][j] == "*") || 
			(i<9 && T[i+1][j] == "*") || 
			(j>0 && T[i][j-1] == "*") || 
			(j<9 && T[i][j+1] == "*")))
			{
				T[i][j] = "p";
			}
		}
	}

	for (i=0; i<10; i++)
	{
  		for (j=0; j<10; j++)
  		{
  			cout << T[i][j] << " ";
  		}
		cout << endl;
  	}
  	return 0;
}

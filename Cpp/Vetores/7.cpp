//Lista 3 do JUDE
//Questão 7

#include <iostream>
using namespace std;

int main() 
{
  int N, XA, XB, XC, D;
  cin >> N;
  D = 0;
  int VA[N];
  int VB[N];
  int VC[N];
  
  for (int i = 0; i < N; i++)
  {
  	cin >> XA;
  	VA[i] = XA;
  }
  
  for (int i = 0; i < N; i++)
  {
  	cin >> XB;
  	VB[i] = XB;
  }
  
  for (int i = 0; i < N; i++)
  {
  	cin >> XC;
  	VC[i] = XC;
  }
  
  for (int i = 0; i < N; i++)
  {
  	if ((VA[i] + VB[i]) == VC[i])
  	{
  		D++;
  	}
  	else
  	{
  		cout << "NOPE :(" << endl;
  		break;
  	}
  }
  
  if (D == N)
  {
  	cout << "OK" << endl;
  }
  
  return 0;
}
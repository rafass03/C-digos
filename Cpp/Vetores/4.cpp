//Lista 3 do JUDE
//Questão 4

#include <iostream>
using namespace std;

int main()
{
    int S, N, P;
    cin >> S >> N;
    int V1[N] = {0};
    
    for (int i = 0; i < S; i++)
    {
        cin >> P;
        for (int j = 0; j < N; j += P)
        {
            V1[j] = 1;
        }
    }
    for (int i = 0; i < N; i++) 
    {
        cout << V1[i] << " ";
    }
return 0;
}
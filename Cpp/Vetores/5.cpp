//Lista 3 do JUDE
//Questão 5

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N, X;
    cin >> N;
    vector <int> V1 (1000001, 0);

    for (int i = 0; i < N; i++)
    {
        cin >> X;
        V1[X] = 1;

    }

    for (int i = 0; i <= 1000000; i++)
    {
        if (V1[i] == 1)
        {
            cout << i << " ";
        }
    }

return 0;
}

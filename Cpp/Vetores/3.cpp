//Lista 3 do JUDE
//Questão 3

#include <iostream>
using namespace std;

int main()
{
    int N, X, M, Vida = 0;
    cin >> N;

    int V1[N];

    for (int i = 0; i < N; i++)
    {
        cin >> X;
        V1[i] = X;
    }

    cin >> M;
    Vida = M;

    for (int i = 0; i < N; i++)
    {
        if (V1[i] == 1)
        {
            M = Vida;
        }
        else if (V1[i] > 1)
        {
            M -= V1[i];
            if (M <= 0)
            {
                break;
            }
        }
        else
        {
            continue;
        }
    }
    if ( M >= 1)
    {
        cout << "Yes, you can" << endl;
    }
    else
    {
        cout << "You Died" << endl;
    }
return 0;
}
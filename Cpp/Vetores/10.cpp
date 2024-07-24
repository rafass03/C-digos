//Lista 3 do JUDE
//Questão 10

#include <iostream>
using namespace std;

int main() 
{
    int N, XA;
    cin >> N;
    int VA [N];
    bool Esferas[7] = {false};
    bool todasEsferas = true;

    for (int i = 0; i < N; i++)
    {
        cin >> XA;
        VA[i] = XA;
    }

    for (int i = 0; i < N; i++)
    {
        int numEsferas = VA[i];
        if (numEsferas >= 1 && numEsferas <= 7)
        {
            Esferas[numEsferas - 1] = true;
        }
    }

    for (int i = 0; i < 7; i++)
    {
        if(Esferas[i])
        {
            cout << i + 1 << " ";
        }
    }
    
    for (int i = 0; i < 7; i++)
    {
        if (Esferas[i] == false)
        {
            todasEsferas = false;
            break;
        }
    }

    cout << endl;

    if (todasEsferas == true)
    {
        cout << "Saia Shenlong e realize o meu desejo" << endl;
    }
    else
    {
        cout << "Nao encontramos todas" << endl;
    }

    return 0;
}

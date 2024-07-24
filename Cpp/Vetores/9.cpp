//Lista 3 do JUDE
//Questão 9

#include <iostream>
using namespace std;

int main() 
{
    int N, Y, XA, XB;
    cin >> N;
    int VA[N];
    int VB[N];
    bool encontrou = false;

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

    cin >> Y;

    for (int i = 0; i < N; i++)
    {
        if (VA[i] == Y)
        {
            cout << VB[i] << " ";
            encontrou = true;
        }
    }

    if (encontrou == false)
        {
            cout << "Nenhum" << endl;
        }

    return 0;
}
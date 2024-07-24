//Lista 3 do JUDE
//Questão 8

#include <iostream>
using namespace std;

int main() {
    int N, XA, XB;
    cin >> N;
    int VA[N];
    int VB[N];
    int VC[N];

    for (int i = 0; i < N; i++) {
        cin >> XA;
        VA[i] = XA;
    }

    for (int i = 0; i < N; i++) {
        cin >> XB;
        VB[i] = XB;
    }

    for (int i = 0; i < N; i++) {
        if (VA[i] == 0)
        {
            VC[i] = 0;
        } 
        else 
        {
            VC[i] = ((VB[i] * 100) / VA[i]);
        }
        cout << VC[i] << " ";
    }

    return 0;
}

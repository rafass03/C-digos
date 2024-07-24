//Lista 3 do JUDE
//Questão 2

#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N, V, E, count;
    string C;
    count = 0;
    cin >> N;

    string V1 [N];
    int V2 [N];

    for (int i = 0; i < N; i++)
    {
        cin >> C >> V;
        V1 [i] = C;
        V2 [i] = V;
    }

    cin >> E;

    for (int i = 0; i < N; i++)
    {
        if(V2 [i] >= E)
        {
            cout << V1[i] << " " << V2[i] << endl;
            count += V2[i];
        }
    }
    if (count >= E)
    {
        cout << count << endl;
    }
    else
    {
        cout << "0" << endl;
    }
return 0;
}
#Prova 4 do JUDE
#Questão 1

N = int(input())
Planetas_Visitados = list(map(int, input().split()))
P = list(map(int, input().split()))

for i in P:
    Esquerda = 0 
    Direita = N - 1
    if i == 0:
        break
    while Esquerda <= Direita:
        Meio = (Esquerda + Direita) // 2
        if Planetas_Visitados[Meio] == i:
            print(Meio)
            break
        elif Planetas_Visitados[Meio] < i:
            Esquerda = Meio + 1
        else:
            Direita = Meio - 1
    else:
        print("Nao foi visitado ainda.")
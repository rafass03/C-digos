#Prova 3 do JUDE
#Questão 1

Z = 0
N = int(input())
matriz = []
for i in range(N):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
C = int(input())
for x in range(C):
    X, Y = map(int, input().split())
    P=int(matriz[X][Y])
    Z = Z + P
print(Z)
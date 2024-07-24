#Prova 3 do JUDE
#Questão 3

contador = 0
N, M = [int(x) for x in input().split()]
matriz = []
for i in range(N):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

for i in range(N):
    if i % 2 == 0: 
        for j in range(M):
            if matriz[i][j] > 0:
                contador += matriz[i][j]
            else:
                contador = max(0, contador + matriz[i][j])
    else:
        for j in range(M-1, -1, -1):
            if matriz[i][j] > 0:
                contador += matriz[i][j]
            else:
                contador = max(0, contador + matriz[i][j])
print(contador)
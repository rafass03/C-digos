#Prova 3 do JUDE
#Questão 2

linhas = 8
colunas = 8
matriz = []
for i in range(linhas):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

X, Y = map(int, input().split())
(matriz[X][Y]) = 1

contador = 0
for i in range(linhas):
    if matriz[X][i] == 2:
        contador += 1
        break
for i in range(colunas):
    if matriz[i][Y] == 2:
        contador += 1
        break
print(contador)
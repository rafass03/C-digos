#Prova 2 do JUDE
#Questão 2

Entrada = input()
Valores = Entrada.split()
N = int(Valores[0])
Q = int(Valores[1])
Valor=0

for x in range(N):
    Valor = Valor + Q
    Q=Q*2
print (Valor)
#Prova 2 do JUDE
#Questão 5

Ataques=0
Entrada = input()
Valores = Entrada.split()
E = int(Valores[0])
P = int(Valores[1])

while E > 0 and P > 0:
    E -= P
    P -= 1
    Ataques = Ataques + 1
if E <= 0:
    print(Ataques)
else:
    print('F')
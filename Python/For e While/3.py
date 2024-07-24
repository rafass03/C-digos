#Lista 3 do JUDE
#Questão 2

N=int(input())
Resultado=0
Tradicional=0
Geleia=0

for x in range (N):
    Resultado=int(input())
    if Resultado == 10:
        Tradicional += 1
    if Resultado == 11:
        Geleia += 1
if Tradicional > Geleia:
    print('Tradicional')
else:
    print('Geleia')
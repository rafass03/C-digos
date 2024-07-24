#Lista 3 do JUDE
#Questão 4

T=int(input())
Resultado=0
for x in range(500):
    P=int(input())
    if P > Resultado:
        Resultado = P
    if P == 0:
        break
if Resultado > T:
    print('ALARME')
else:
    print('O Havai pode dormir tranquilo')
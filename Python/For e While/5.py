#Lista 3 do JUDE
#Questão 3

N=int(input())
Resultado=0

for x in range (N):
    P=int(input())
    if P > Resultado:
        Resultado = P
print(Resultado)
#Prova 2 do JUDE
#Questão 1

N=int(input())
Valor=0
for x in range(N):
    C,P =(input()).split()
    Valor = Valor + (int(C)*float(P))
print (format((Valor),'.2f'))
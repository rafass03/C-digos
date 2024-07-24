#Lista 3 do JUDE
#Questão 1

N=int(input())
DanoFinal=0

for x in range (N):
    P,M=(input()).split()
    DanoFinal=int(P)+int(M)
    print(DanoFinal)
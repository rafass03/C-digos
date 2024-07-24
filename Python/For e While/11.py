#Lista 3 do JUDE
#Questão 6

P=int(input())
Z = 0

while (P-Z) > 0:
    Z += 1
    for x in range(P-Z):
        print('>', end='')
    for x in range (P-(P-Z)):
        print('#', end="")
    print('')
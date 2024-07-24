#Lista 3 do JUDE
#Questão 7

N=int(input())
Nivel = 1

for x in range(N):
    Y,X =(input()).split()

    if Y == 't' and 1 <= int(X) <= 2:
        Nivel += int(X)
        if Nivel == 5:
            print('Aventura concluida')
            break

    elif Y == 'm' and 1 <= int(X) <= 5:
        print('Combate iniciado')
        if Nivel >= int(X):
            Nivel += 1
            print('VITORIA')
            if Nivel == 5:
                print('Aventura concluida')
                break
        else:
            print('Derrota! Fim da aventura')
            break

    elif Y == 'b' and 1 <= int(X) <= 2:
        Nivel -= int(X)
        if Nivel <=0:
            Nivel = 0
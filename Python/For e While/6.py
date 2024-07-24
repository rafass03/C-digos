#Prova 2 do JUDE
#Questão 3

cor_anterior = ""
cor_atual = input()

while True:
    if cor_anterior != "":
        if cor_anterior == cor_atual:
            print (cor_anterior)
        elif (cor_anterior == "azul" and cor_atual == "verde") or (cor_atual == "azul" and cor_anterior == "verde"):
            print ("ciano")
        elif (cor_anterior == "amarelo" and cor_atual == "verde") or (cor_atual == "amarelo" and cor_anterior == "verde"):
            print ("lima")
        elif (cor_anterior == "vermelho" and cor_atual == "verde") or (cor_atual == "vermelho" and cor_anterior == "verde"):
            print ("marrom")
        elif (cor_anterior == "vermelho" and cor_atual == "azul") or (cor_atual == "vermelho" and cor_anterior == "azul"):
            print ("roxo")
        elif (cor_anterior == "azul" and cor_atual == "amarelo") or (cor_atual == "azul" and cor_anterior == "amarelo"):
            print ("verde")
        elif (cor_anterior == "vermelho" and cor_atual == "amarelo") or (cor_atual == "vermelho" and cor_anterior == "amarelo"):
            print ("laranja")
    if cor_atual == 'preto':
        print('Game Over')
        break
    elif cor_atual == 'branco':
        break
    cor_anterior = cor_atual
    cor_atual = input()

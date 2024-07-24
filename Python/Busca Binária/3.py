# Prova 4 do JUDE
# Questão 3

qtd_datas_importantes = int(input())

datas_importantes = [()] * qtd_datas_importantes

for i in range(qtd_datas_importantes):
    data, local = input().split()
    data = int(data)

    datas_importantes[i] = (data, local)

qtd_tentativas = int(input())

mundo_salvo = False

salto_realizado = False

for i in range(qtd_tentativas):
    tentativa = int(input())

    inicio = 0
    fim = qtd_datas_importantes - 1
    indice = (inicio + fim) // 2
    data_exata = False

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if (datas_importantes[meio][0] == tentativa):
            indice = meio
            data_exata = True
            break
        else:
            if (inicio == fim):
                if (datas_importantes[meio][0] > tentativa): 
                    indice = meio if abs(tentativa - datas_importantes[meio][0]) <= abs(tentativa - datas_importantes[max(meio - 1, 0)][0]) else max(meio - 1, 0)
                else: 
                    indice = meio if abs(tentativa - datas_importantes[min(meio + 1, qtd_datas_importantes - 1)][0]) > abs(tentativa - datas_importantes[meio][0]) else min(meio + 1, qtd_datas_importantes - 1)
            if (datas_importantes[meio][0] < tentativa):
                

                inicio = meio + 1
            elif (datas_importantes[meio][0] > tentativa):
                
                fim = meio - 1
    
    if (datas_importantes[indice][0] == 19631125 and not mundo_salvo):
        salto_realizado = True
        if (datas_importantes[indice][1] == 'dallas'): 
            
            mundo_salvo = True
            

if (salto_realizado):
    print('Salto temporal realizado')
    if (not mundo_salvo):
        print('Ops. local errado')

if (mundo_salvo):
    print('O mundo foi salvo')
else: print('Fim do mundo')
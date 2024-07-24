# Prova 4 do JUDE
# Questão 2

def busca(x, y):
  baixo, alto = 0, len(x) - 1

  while baixo <= alto:
      meio = (baixo + alto) // 2
      if x[meio] == y:
          return meio
      elif x[meio] < y:
          baixo = meio + 1
      else:
          alto = meio - 1
  return -1

Abates_Plantas = 0
Abates_Jogador = 0
Q, Z = map(int, input().split())
Plantas = input().split()
N = list(map(int, input().split()))
Zumbis = []

for x in range(Z):
    linha = input().split()
    Zumbis.append(linha)

for i in range(Z):
    Index = busca(Plantas, Zumbis[i][0])
    if Index != -1:
        if int(Zumbis[i][1]) == N[Index]:
            Abates_Plantas += N[Index]
        elif int(Zumbis[i][1]) < N[Index]:
            Abates_Plantas += int(Zumbis[i][1])
        elif int(Zumbis[i][1]) > N[Index]:
            Abates_Plantas += N[Index]
            Abates_Jogador += int(Zumbis[i][1]) - N[Index]
    else:
        Abates_Jogador += int(Zumbis[i][1])
print("Plantas:", Abates_Plantas)
print("Eu:", Abates_Jogador)
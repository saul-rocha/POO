import random

lista = []
aposta = {1: [], 2: [], 3: []}
cont = 0
for a in range(13):
    lista.append(random.randrange(1, 4))
    aposta[1].append(random.randrange(1, 4))
    aposta[2].append(random.randrange(1, 4))
    aposta[3].append(random.randrange(1, 4))

print(lista, "\n", aposta[1],"\n", aposta[2], "\n", aposta[3])
for a in range(1,4):
    for b in range(13):
      if lista[b] == aposta[a][b]:
          cont += 1

    if cont == 13:
        print("apostador {} é um ganhador!".format(a))
        print("apostador {}: {} acertos".format(a, cont))
    else:
        print("apostador {}: {} acertos".format(a, cont))
    cont = 0




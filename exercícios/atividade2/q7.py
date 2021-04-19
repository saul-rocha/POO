
lista1 = []
lista2 = []
lista3 = []
#ler as listas com 10 elementos
for a in range(10):
    valor = int(input("elemento da lista1: "))
    lista1.append(valor)

for a in range(10):
    valor = int(input("elemento da lista2: "))
    lista2.append(valor)

#multiplica dois valores
def mult(x,y):
    return x*y

#cria uma terceira lista com o produto de cada elemeto das listas
for a in range(10):
    lista3.append(mult(lista1[a], lista2[a]))

print(lista3)
import functools as ft
lista = []

##preenche a lista de 1 até 100
for a in range(1, 101):
    lista.append(a)

def soma(a, b):
    return a+b

media = (ft.reduce(soma, lista))/len(lista)

def mediana(a):
    tam = len(a) // 2
    #se qtd de elementos for par, mediana == media dos dois elementos do meio
    if (tam % 2) == 0:
        ma = (a[tam] + a[tam-1]) / 2
    #se nao mediana == elemento do meio
    else:
        ma = (a[tam])

    return float(ma)

def variancia(a,media):
    var_a = 0
    tam = len(a)
    # subtrai todos os elementos com a media e eleva ao quadrado, armazenando em dp
    for b in a:
        var_a += (b - media)**2
    # variancia é o resultado das somas divido pela qtd de elementos
    var_a = ((var_a) / tam)

    return var_a

def desvio(varian):
    # dp é a variancia elevado a "meio(1/2) que equivale a raiz quadrada"
    dp = (varian) ** (1/2)

    return dp

print(lista)
medianares = mediana(lista)
var_a = variancia(lista,media)
dp = desvio(var_a)
print("media = {}\nmediada: {}\nvariancia: {:.1f}\ndesvio padrao: {:.1f}".format(media, medianares, var_a, dp))




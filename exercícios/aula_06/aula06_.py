'''
lista = []

def isZero(x):
    return x==0

def par(x):
    return x % 2 == 0 and x != 0

def impar(x):
    return x % 2 != 0

while True:
    a = int(input("digite um numero: "))

    if a < 0:
        break
    lista.append(a)

par = list(filter(par,lista))
imparr = list(filter(impar,lista))
zero = list(filter(isZero,lista))

par.sort()
imparr.sort()

lista = par + zero + imparr

print(lista)
'''
'''
import functools as ft

def soma(a, b):
    return a + b

def par(a):
    return a % 2 == 0

lista = [1,2,3,4,5,6,7,8,9,10]

lista = filter(par,lista)

n = ft.reduce(soma,lista)
'''

lista = []

while True:
    a = int(input("digite um numero: "))

    if a < 0:
        break
    lista.append(a)

par = list(filter(lambda a: a % 2 == 0, lista))
impar = list(filter(lambda a: a % 2 != 0, lista))
zero = list(filter(lambda a: a == 0, lista))

par.sort()
impar.sort()

lista = par + zero + impar

print(lista)
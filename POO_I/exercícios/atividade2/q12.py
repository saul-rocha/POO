import functools as ft

corredores = {}

def soma(a,b):
    return a+b

volta = 0
nome = input("nome: ")
tempo1 = float(input("tempo na 1a volta: "))
tempo2 = float(input("tempo na 2a volta: "))
if tempo1 > tempo2:
    melhor = tempo2
    mn = nome
    melhorvolta = volta + 2
    volta = 0
else:
    melhor = tempo1
    mn = nome
    melhorvolta = volta + 1
    volta = 0
tempo3 = float(input("tempo na 3a volta: "))
if tempo3 < melhor:
    melhor = tempo3
    mn = nome
    melhorvolta = volta + 3
    volta = 0
corredores[nome] = [tempo1, tempo2, tempo3]

for a in range(1,5):
    nome = input("nome: ")
    tempo1 = float(input("tempo na 1a volta: "))
    if tempo1 < melhor:
        melhor = tempo1
        mn = nome
        melhorvolta = volta + 1
        volta = 0
    tempo2 = float(input("tempo na 2a volta: "))
    if tempo2 < melhor:
        melhor = tempo2
        mn = nome
        melhorvolta = volta + 2
        volta = 0
    tempo3 = float(input("tempo na 3a volta: "))
    if tempo3 < melhor:
        melhor = tempo3
        mn = nome
        melhorvolta = volta + 3
        volta = 0
    corredores[nome] = [tempo1, tempo2, tempo3]

#falta pegar o campeao

print("melhor tempo: ", mn,"\nVolta Nº: ", melhorvolta)


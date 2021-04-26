import functools as ft

alunos = {}

for a in range(3):
    nome = input("nome: ")
    nota1 = float(input("nota1: "))
    nota2 = float(input("nota1: "))
    alunos[nome] = nota1, nota2

def med(a,b):
    return (a + b)/2

x = input("nome do aluno: ")

media = ft.reduce(med, alunos[x])

print(media)
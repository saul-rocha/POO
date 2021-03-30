"""
WHILE
a = 0
while a < 40:
    if (a % 4 == 0) or (a % 10 == 0):
        print("PIN")
    else:
        print(a)
    a += 1

print("FIM")
"""

"""
FOR

numero = [1,2,3,4,5]
cidade = ["Picos", "Teresina"]

for a in numero:
    print(a)


for x in range(0,10,2):#0=inicio da lista 10=final da lista 2 = incremento
    print(x)
"""
"""TABUADA de multiplicação
for a in range(1,10):
    print("-------------")
    for b in range(1,11):
        print("{} * {} = {}".format(a, b, a*b))
"""

"""try except
a = 10
b = 0
try:
    c = a/b
except:
    print("nao existe divisão por 0")

print(c)




a = 10
b=5

try:
    assert a>b #força um erro
    print(a/b)
except:
    print("o valor de a é menor que b")

try:
    assert isinstance(a,float)
except:
    print("a variavel nao é float")

"""
"""FUNCTIONS

def soma(a,b):
    c = a + b
    return c #pode retornar quantos valores quiser


c = soma(10,5)

print(c)
"""
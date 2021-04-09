
# Strings
'''
nome = 'Flavio'
sobrenome = 'Araujo'
a = 10

nome_completo = nome + ' ' + str(a) + sobrenome

print(nome_completo)

for c in nome_completo:
    print(c)

'''


''' 
completo = '{a}, {b}, texto, {c}'
print(completo.format(a = 2, b = 'Henrique', c = 'Araujo'))
'''

''' 
str = 'Flavio Henrique Duarte de Araujo'

nomes = str.split('a')
print(nomes)
'''

''' 
numeros = input('Digite valores: ')
numeros = numeros.split(' ')
print(numeros)
'''

''' 
str = 'flavio henrique duarte'

print(str.title())
'''


#Listas
''' 
frutas = ['manga', 'uva', 'uva', 'banana', 'laranja', [1, 2, 3, 4]]
numeros = [4, 2, 3, 10, 2]

lista_aux = frutas[-1]

for posicao in lista_aux:
    print(posicao)
'''
''' 
l1 = [1, 2]
l2 = []
l3 = [4, 5]

l1.extend(l2)
l1.extend(l3)
print(l1)
'''
#frutas.append(numeros)
#frutas.extend(numeros)

#frutas.insert(3, 'goiaba')
#frutas[3] = 'maça'

#p = frutas.count('banana')

#print(frutas, p)

#lista = frutas[-1]

#print(lista)



''' 
frutas.append('morango')
#a = frutas.pop(2)
frutas.remove('uva')
frutas.sort()
print(frutas)

numeros.sort()
print(numeros)
'''

par = []
impar = []
zeros = []
n = 0

while True:
    n = int(input('digite um numero: '))

    if n < 0:
        break
    elif n == 0:
        zeros.append(n)
    elif n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()

print(par + zeros + impar)


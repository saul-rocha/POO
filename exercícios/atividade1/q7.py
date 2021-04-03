dec = int(input("Digite um numero: "))

b = ""
# faz uma lista de caracteres com os restos das divisẽos
while dec != 0:
    b = b + str(dec%2)
    dec = int(dec / 2)

print(b[::-1]) #imprime a lista a partir do ultimo elemento
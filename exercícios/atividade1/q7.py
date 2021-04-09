

def binario(n):
    b = ""
    while n > 0:
        b += str(n%2) #resto da divisão
        n = int(n//2) #divisão inteira
    return b

dec = int(input("Digite um numero: "))

bina = binario(dec)
print(bina[::-1])#imprime a lista a partir do ultimo elemento

n = int(input("digite um numero: ")) #ler o primeiro valor de n
#a recebe 1 pois irá efetuar uma multiplicação
a = 1

while n > 0 and n < 16:
    while (n > 0):
        a *= n
        n -= 1
    print("Fatorial = ", a)
    a = 1 # reseta a variavel a
    n = int(input("digite um numero: "))# ler um novo valor para n


    
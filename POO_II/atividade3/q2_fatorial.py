num = int(input("Fatorial de: "))
#com recursividade
def fatorialR(num,res=1):# possui dois parametro, num é o valor para calcular o fatorial e res é predifinido como um pois irá efetuar uma multiplicação
    if (num > 0):# condição de parada da recursão

        res = fatorialR(num-1,res*num) # num é decramentado na passagem de parâmetro e res acumula o resultado do produto

    return res #retorna o resultado do fatorial


print("Fatorial Recursivo", fatorialR(num))


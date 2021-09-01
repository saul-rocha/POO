#calculo do fatorial
def fatorialR(num,res=1):# possui dois parametro, num é o valor para calcular o fatorial e res é predifinido como um pois irá efetuar uma multiplicação
    if (num > 0):# condição de parada da recursão 
        res = fatorialR(num-1,res*num) # num é decramentado na passagem de parâmetro e res acumula o resultado do produto

    return res #retorna o resultado do fatorial


n = int(input("Valor de n: "))
p = int(input("Valor de p: "))

a = fatorialR(n) / fatorialR(n-p)

c = fatorialR(n) / (fatorialR(p)*(fatorialR(n-p)))

print("Arranjo = {}\nCombinação= {}".format(a,c))

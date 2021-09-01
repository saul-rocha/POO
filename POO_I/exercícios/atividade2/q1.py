def tamString(s):
    cont = 0 #inicia com 0, pois efetua uma soma
    for a in s:
        cont += 1 # para cada elemento da string será iterado 1 a variavel cont
    return cont

print(tamString("lenimprovisada"))
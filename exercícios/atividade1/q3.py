#inicia esc com 1 para poder entrar no while
esc = 1

#condição de parada
while (esc > 0) and (esc < 4):
    print("1- TRIANGULO\n2- QUADRADO\n3- CIRCULO\n4- SAIR")
    esc = int(input("Escolha uma opção: "))
    if esc == 1:
        b = int(input("base: "))
        h = int(input("altura: "))
        print("Area do triângulo= {}".format((b*h)/2))
        continue   #sempre que entrar nessa condição volta para o inicio do while lendo a escolha novamente
    elif esc == 2:
        b = int(input("base: "))
        h = int(input("altura: "))
        print("Area do quadrado = {}".format((b*h)*(b*h)))
        continue #idem anterior
        
    elif esc == 3:
        r = float(input("Raio: "))
        print("Area do Circulo = {}".format(3.14 * (r*r)))
        continue #idem anterio
        
    else:
        print("SAIU")
        break # caso nao entre em nenhuma das condições acima o programa para

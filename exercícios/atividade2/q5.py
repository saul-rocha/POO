import random

#gera um numero aleatorio de 0 a 100
def gerador():
    return random.randrange(0,101)

sorteado = gerador()
cont = 0 # numero da tentativa
chances = 0 # numero de chances
while chances < 10: # codição de parada para caso o usuario errar todas as tentativas
    esc = int(input("Digite um numero: "))
    if(esc == sorteado): # se numero digitado for igual ao sorteado
        print("Acertou!")
        op = int(input("1- continuar\n2- sair\n"))

        if op == 2: # para a execução
            break

        #caso o jogo for proceder é gerado um nuvo numero e as checes e tentativas sao resetadas
        sorteado = gerador()
        cont = 0
        chances = 0

    else: #caso erre a tentativa, incrementa a tentativa e as chances
        chances += 1
        cont += 1
        print("tentativa: ", cont) # numero da tentativa

from src.elevador import Elevador

while True:
    print("1 - Inicializar")
    print("2 - Entra")
    print("3 - Sai")
    print("4 - Sobe")
    print("5 - Desce")
    print("0 - Sair")
    esc = int(input("Digite uma opção: "))

    ##Inicia o elevador
    if esc == 1:
        total_andares = int(input("Total de Andares: "))
        capacidade = int(input("Papacidade do Elevador: "))
        elevador =  Elevador(total_andares, capacidade)
        print("Iniciado!")
       
    ##adiciona pessoa ao elevador
    elif esc == 2:
        res = elevador.entra()
        if res:
            print("1 Pessoa Entrou no Elevador no Andar:", elevador.andar_atual)
            print("Pessoas no Elevador:", elevador.qtdpessoa)
        else:
            print("Elevador Lotado!")
    ##retira pessoa do elevador
    elif esc == 3:
        res = elevador.sai()
        if res:
            print("1 Pessoa Saiu do Elevador no Andar:", elevador.andar_atual)
            print("Pessoas no Elevador:", elevador.qtdpessoa)
        else:
            print("Elevador Vazio!")
    ##sobe elevador
    elif esc == 4:
        res = elevador.sobe()
        if res:
            print("Elevador Subiu para o Andar:", elevador.andar_atual)
            print("Pessoas no Elevador:", elevador.qtdpessoa)
        else:
            print("Elevador No Último Andar!")

    ## desce elevador
    elif esc == 5:
        res = elevador.desce()
        if res:
            print("Elevador Desceu para o Andar:", elevador.andar_atual)
            print("Pessoas no Elevador:", elevador.qtdpessoa)
        else:
            print("Elevador No Térreo!")
    elif esc == 0:
        break
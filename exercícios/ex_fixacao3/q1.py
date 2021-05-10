from src.pessoa import Pessoa

while True:
    print("1 - Ler pessoa")
    print("2 - Imprimir Pessoa")
    print("3 - Calcular idade")
    print("4 - Alterar Pessoa")
    print("0 - Sair")
    esc = int(input("Digite uma opção: "))
    if esc == 1:
        nome = input("Nome: ")
        altura = float(input("Altura: "))
        print("Data de nascimento")
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        pessoa = Pessoa(nome, altura, dia, mes, ano)
    elif esc == 2:
        pessoa.imprimir
    elif esc == 3:
        print("Idade: ", pessoa.idade())
    elif esc == 4:
        print("1 - Alterar nome\n2 - Alterar Altura\n3 - Alterar Data de Nascimento")
        alt = int(input("Digite uma opção: "))
        if alt == 1:
            novonome = input("Novo Nome: ")
            pessoa.nome = novonome
        elif alt == 2:
            novaaltura = input("Nova Altura: ")
            pessoa.altura = novaaltura
        elif alt == 3:
            novodia = int(input("Novo Dia: "))
            novomes = int(input("Novo Mês: "))
            novoano = int(input("Novo Ano: "))
            pessoa.ano = novoano
            pessoa.dt_nasc = "{}/{}/{}".format(novodia,novomes,novoano)
    elif esc == 0:
        break;
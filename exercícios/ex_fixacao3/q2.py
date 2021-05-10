from src.pessoa2 import Agenda
##inicia a agenda
agenda = Agenda()

while True:
    print("1 - Armazenar Pessoa")
    print("2 - Imprimir Agenda")
    print("3 - Busca Pessoa")
    print("4 - Imprimir Pessoa")
    print("5 - Remover Pessoa")
    print("0 - Sair")
    esc = int(input("Digite uma opção: "))

    ##armazena uma pessoa
    if esc == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        res = agenda.armazenaPessoa(nome, idade, altura)
        if res:
            print("Adicionado!")
        else:
            print("Agenda Lotada!")
    ##imprime toda a agenda
    elif esc == 2:
        agenda.imprimeAgenda()
    ##dado o nome de uma pessoa devolve o indice da pessoa na agenda
    elif esc == 3:
        nome = input("Nome: ")
        index = agenda.buscaPessoa(nome)
        print("Index de", nome,": ", index)

    elif esc == 4:
        id = int(input("Index da Pessoa: "))
        agenda.imprimePessoa(id)

    ## remove uma pessoa pelo nome
    elif esc == 5:
        nome = input("Nome: ")
        res = agenda.removePessoa(nome)
        if res:
            print("Removido!")
        else:
            print("Não encontrado!")
    elif esc == 0:
        break;
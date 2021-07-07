from pessoa import Motorista, Assistente, Gerente
from auth import SistemaInterno
from sistema import Sistema
from viagem import Viagem

def add_assistente():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salario: "))

    a = Assistente(nome, idade, cpf, salario)
    s.add_assistente(a)

def add_motorista():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salario: "))
    cnh = input("Nivel CNH: ")

    m = Motorista(nome, idade, cpf, salario, cnh)
    s.add_motorista(m)

def consultar_funcionarios():
    s.consultar_funcionarios()

def fazer_viagem(id):

    local_saida = input("Local de Saída: ")
    local_destino = input("Local de Destino: ")
    cpf_motorista = input("CPF do motorista: ")
    if cpf_motorista in s.motoristas.keys():
        v = Viagem(local_saida, local_destino, cpf_motorista)
        s.fazer_viagem(v, id)
    else:
        print("Motorista não existe!")

def mostrar_historico_viagens():
    s.mostrar_viagens()

def mostrar_historico_viagem(id_viagem):
    s.viagens[id_viagem].mostrar_viagem()

def menu():
    print("1 - Adicionar Assistente")
    print("2 - Adicionar Motorista")
    print("3 - Consultar Funcionarios")
    print("4 - Fazer Viagem")
    print("5 - Mostrar Historico de Viagens")
    print("6 - Mostrar Historico de uma viagem")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    return opcao

s = Sistema()

gerente = Gerente("Damião", 39, "1234", "a", "1")
si = SistemaInterno()
id = 1

while True:
    op = menu()

    if op == 1:
        login = input("Login: ")
        senha = input("Senha: ")
        if si.login(gerente, login, senha):
            add_assistente()
        else:
            print("Não autorizado!")
    elif op == 2:
        login = input("Login: ")
        senha = input("Senha: ")
        if si.login(gerente, login, senha):
            add_motorista()
        else:
            print("Não autorizado!")

    elif op == 3:
        consultar_funcionarios()


    elif op == 4:
        print(s.viagens.keys())
        fazer_viagem(id)
        print(s.viagens.keys())
        while True:
            nome = input("Nome do Passageiro: ")
            valor = float(input("Valor da Passagem: "))
            s.viagens[id].add_cliente(nome, valor)

            continuar = int(input("Deseja continuar? (1 - SIM || 0 - NÃO): "))
            if continuar == 0:
                break
        id +=1
    elif op == 5:
        mostrar_historico_viagens()

    elif op == 6:
        id_v = int(input("Id da viagem: "))
        s.viagens[id_v].mostrar_viagem()

    elif op == 0:
        break

    else:
        print("Opção Inválida!")

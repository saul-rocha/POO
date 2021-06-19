from pessoa import Pessoa, Funcionario, Cliente
from banco import Banco
from conta import ContaCorrente, ContaPoupanca, SeguroDeVida
from tributavel import Tributavel


def menu():
    print("\n\n")
    print("1....Cadastrar Funcionário")
    print("2....Cadastrar Cliente")
    print("3....Criar Conta Corrente")
    print("4....Criar Conta Poupança")
    print("5....Criar Seguro de Vida")
    print("6....Cobrar Tributação")
    print("7....Sacar")
    print("8....Depositar")
    print("9....Transferir")
    print("10...Imprimir Historico de Uma Conta")
    print("11...Exibir Informações do Banco")
    print("12...Sair")

    res = int(input("Digite uma opção: "))

    return res

def cadastrar_funcionario():
    print("DIGITE OS DADOS DO FUNCIONÁRIO")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nascimento = input("Data de Nascimento: ")
    salario = float(input("Salário: "))

    p = Pessoa(nome, cpf, dt_nascimento)
    f = Funcionario(p, salario)
    banco.adicionar_funcionario(f)


def cadastrar_cliente():
    print("DIGITE OS DADOS DO CLIENTE")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nascimento = input("Data de Nascimento: ")
    profissao = input("Profissão: ")
    renda = float(input("Renda: "))

    p = Pessoa(nome, cpf, dt_nascimento)
    c = Cliente(p, profissao, renda)
    banco.adicionar_cliente(c)

def cadastrar_conta_corrente():
    banco.mostrar_clientes()

    cpf = input("CPF do Cliente: ")

    numero = input("Numero da Conta: ")
    saldo = float(input("Saldo da Conta: "))
    limite = float(input("Limite: "))
    cc = ContaCorrente(banco.get_cliente(cpf), numero, saldo, limite)
    banco.adicionar_conta_corrente(cc)
    print("Conta Corrente Criada Com Sucesso!")


def cadastrar_conta_poupanca():
    banco.mostrar_clientes()

    cpf = input("CPF do Cliente: ")

    numero = input("Numero da Conta: ")
    saldo = float(input("Saldo da Conta: "))

    cp = ContaPoupanca(banco.get_cliente(cpf), numero, saldo)
    banco.adicionar_conta_poupanca(cp)
    print("Conta Poupança Criada Com Sucesso!")


def cadastrar_seguro_de_vida():

    banco.mostrar_clientes()

    cpf = input("CPF do Cliente: ")

    valor_mensal = float(input("Valor Mensal: "))
    valor_total = float(input("Valor Total: "))

    sv = SeguroDeVida(banco.adicionar_cliente(cpf), valor_mensal, valor_total)
    banco.adicionar_seguro_de_vida(sv)

def sacar():

    banco.mostrar_clientes()
##saca pelo cpf do cliente
    cpf = input("CPF do Cliente: ")

    valor = float(input("Valor: "))

    if cpf in banco.lista_contas_poupancas.keys() and cpf in banco.lista_contas_correntes.keys():
        escolha = int(input("1 - Conta Poupança || 2 - Conta Corrente: "))

        if escolha == 1:
            banco.sacar(cpf, banco.lista_contas_poupancas(cpf), valor)
        else:
            banco.sacar(cpf, banco.lista_contas_correntes(cpf), valor)





banco = Banco()
#Tributavel.register(ContaCorrente)
#Tributavel.register(SeguroDeVida)


cadastrar_cliente()

cadastrar_conta_corrente()



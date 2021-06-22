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

    f = Funcionario(nome, cpf, dt_nascimento, salario)
    res = banco.adicionar_funcionario(f)
    if res:
        print("Cadastrado")
    else:
        print("Não foi possivel cadastrar")

def cadastrar_cliente():
    print("DIGITE OS DADOS DO CLIENTE")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nascimento = input("Data de Nascimento: ")
    profissao = input("Profissão: ")
    renda = float(input("Renda: "))

    c = Cliente(nome, cpf, dt_nascimento, profissao, renda)
    res = banco.adicionar_cliente(c)
    if res:
        print("Cadastrado")
    else:
        print("Não foi possivel cadastrar")


def cadastrar_conta_corrente():


    cpf = input("CPF do Cliente: ")


    numero = input("Numero da Conta: ")
    saldo = float(input("Saldo da Conta: "))
    limite = float(input("Limite: "))
    cc = ContaCorrente(numero, saldo, limite)
    res = banco.adicionar_conta_corrente(cpf, cc)
    if res:
        lista_tributos.append(cc)
        print("Cadastrado")
    else:
        print("Não foi possivel cadastrar")


def cadastrar_conta_poupanca():


    cpf = input("CPF do Cliente: ")

    numero = input("Numero da Conta: ")
    saldo = float(input("Saldo da Conta: "))

    cp = ContaPoupanca(numero, saldo, 0.0)
    res = banco.adicionar_conta_poupanca(cpf, cp)
    if res:
        print("Cadastrado!")
    else:
        print("Não foi possivel cadastrar")


def cadastrar_seguro_de_vida():

    cpf = input("CPF do Cliente: ")

    valor_mensal = float(input("Valor Mensal: "))
    valor_total = float(input("Valor Total: "))

    sv = SeguroDeVida(valor_mensal, valor_total)
    res = banco.adicionar_seguro_de_vida(cpf, sv)
    if res:
        lista_tributos.append(sv)
        print("Cadastrado")
    else:
        print("Não foi possivel cadastrar")

def sacar():
    ##saca pelo cpf do cliente
    cpf = input("CPF do Cliente: ")
    valor = float(input("Valor do Saque: "))

    if cpf in banco.lista_contas_poupancas.keys() and cpf in banco.lista_contas_correntes.keys():
        escolha = int(input("1 - Conta Poupança || 2 - Conta Corrente: "))
        if escolha == 1:
            banco.lista_contas_poupancas[cpf].sacar(valor)
            print("Saque Efetuado!")
        else:
            banco.lista_contas_correntes[cpf].sacar(valor)
            print("Saque Efetuado!")

    elif cpf in banco.lista_contas_poupancas.keys():
        if banco.lista_contas_poupancas[cpf].sacar(valor):
            print("Saque Efetuado!")
    elif cpf in banco.lista_contas_correntes.keys():
        banco.lista_contas_correntes[cpf].sacar(valor)
        print("Saque Efetuado!")
    else:
        print("Não foi possivel Sacar! Cliente Não possui conta!")

def depositar():
    ##saca pelo cpf do cliente
    cpf = input("CPF do Cliente: ")
    valor = float(input("Valor do Deposito: "))

    if cpf in banco.lista_contas_poupancas.keys() and cpf in banco.lista_contas_correntes.keys():
        escolha = int(input("1 - Conta Poupança || 2 - Conta Corrente: "))
        if escolha == 1:
            banco.lista_contas_poupancas[cpf].deposita(valor)
            print("Depósito Efetuado!")
        else:
            banco.lista_contas_correntes[cpf].deposita(valor)
            print("Depósito Efetuado!")

    elif cpf in banco.lista_contas_poupancas.keys():
        banco.lista_contas_poupancas[cpf].deposita(valor)
        print("Depósito Efetuado!")
    elif cpf in banco.lista_contas_correntes.keys():
        banco.lista_contas_correntes[cpf].deposita(valor)
        print("Depósito Efetuado!")
    else:
        print("Não foi possivel Sacar! Cliente Não possui conta!")


def transferir():
    ##saca pelo cpf do cliente
    cpf = input("CPF do Cliente: ")
    cpf_d = input("CPF destino: ")
    valor = float(input("Valor do Deposito: "))

    if cpf in banco.lista_contas_poupancas.keys() or cpf in banco.lista_contas_correntes.keys():
        escolha = int(input("1 - Conta Poupança || 2 - Conta Corrente: "))
        if escolha == 1:
            if cpf_d in banco.lista_contas_poupancas.keys() or cpf_d in banco.lista_contas_correntes.keys():
                escolha = int(input("1 - Conta Poupança || 2 - Conta Corrente: "))
                if escolha == 1:
                    banco.lista_contas_poupancas[cpf].trasnferir(banco.lista_contas_poupancas[cpf_d], valor)
                    print("Transferencia Efetuada!")
                else:
                    banco.lista_contas_poupancas[cpf].trasnferir(banco.lista_contas_correntes[cpf_d], valor)
                    print("Transferencia Efetuada!")

        else:
            if cpf_d in banco.lista_contas_poupancas.keys() or cpf_d in banco.lista_contas_correntes.keys():
                escolha = int(input("1 - Conta Poupança || 2 - Conta Corrente: "))
                if escolha == 1:
                    banco.lista_contas_correntes[cpf].trasnferir(banco.lista_contas_correntes[cpf_d], valor)
                    print("Transferencia Efetuada!")
                else:
                    banco.lista_contas_correntes[cpf].trasnferir(banco.lista_contas_poupancas[cpf_d], valor)
                    print("Transferencia Efetuada!")
    else:
        print("Não é Possivel Fazer a Transferencia!!")


def mostrar_historico():
    cpf = input("CPF do Cliente: ")

    if cpf in banco.lista_contas_correntes.keys() and banco.lista_contas_correntes.keys():
        banco.mostrar_historico_contac(cpf)
        banco.mostrar_historico_contap(cpf)
    elif cpf in banco.lista_contas_correntes.keys():
        banco.mostrar_historico_contac(cpf)
    elif cpf in banco.lista_contas_correntes.keys():
        banco.mostrar_historico_contap(cpf)
    else:
        print("Conta inexistente")


banco = Banco()
Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)


c = Cliente("Saul", "1", "10012001", "estudante", 400.0)
c1 = Cliente("Flavio", "2", "12121990", "professor", 10000.0)
banco.adicionar_cliente(c)
banco.adicionar_cliente(c1)
cp = ContaPoupanca("123", 35.0)
cc = ContaCorrente("321", 760340.0, 1000000.0)
cc1 = ContaCorrente("1234", 16.0, 2000.0)
sv = SeguroDeVida(200.0, 50000.0)
banco.adicionar_conta_poupanca("1", cp)
banco.adicionar_conta_corrente("2", cc)
banco.adicionar_seguro_de_vida("2", sv)
banco.adicionar_conta_corrente("1", cc1)

num_trib = 1
lista_tributos = []
lista_tributos.append(cc)
lista_tributos.append(sv)

while True:
    op = menu()

    if op == 1:
        cadastrar_funcionario()
    elif op == 2:
        cadastrar_cliente()
    elif op == 3:
        cadastrar_conta_corrente()
    elif op == 4:
        cadastrar_conta_poupanca()
    elif op == 5:
        cadastrar_seguro_de_vida()
    if op == 6:
        num_trib = banco.calcular_tributos(lista_tributos, num_trib)
        banco.imprimir_historico_tributacoes()
    elif op == 7:
        sacar()
    elif op == 8:
        depositar()
    elif op == 9:
        transferir()
    elif op == 10:

        mostrar_historico()
    elif op == 11:
        banco.imprimir_banco()
    elif op == 12:
        break

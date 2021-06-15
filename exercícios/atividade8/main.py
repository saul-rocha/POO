from funcionario import Funcionario
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from historico import Historico
from seguro_de_vida import SeguroDeVida
from tributavel import Tributavel
from cobrar_tributacao import CobrarTributacao

def menu():
    print("1 - Cadastrar Funcionário\n2 - Cadastrar Cliente\n3 - Criar Conta Corrente\n4 - Criar Conta Poupança\n5 - Criar Seguro de Vida\n"
          "6 - Cobrar Tributação\n7 - Sacar\n8 - Depositar\n9 - Transferir\n10 - imprimir Historico\n11 - Status do Banco\n0 - Sair")
    esc = int(input("Digite uma opção: "))

    return esc

banco_funcionarios = {}
banco_clientes = {}
banco_CC = {}
banco_CP = {}
banco_SV = {}



while True:
    op = menu()

    if op == 1:#funcionario
        print('Informe os dados do Funcionario: ')
        nome = input('Infrome o nome: ')
        cpf = input('Informe o CPF: ')
        dt_nascimento = input('Informe a data de nascimento: ')
        salario = float(input('Informe o salario: '))
        banco_funcionarios.setdefault(cpf, Funcionario(nome, cpf, dt_nascimento, salario))

    elif op == 2:#cliente
        print('Informe os dados do Cliente: ')
        nome = input('Informe o nome: ')
        cpf = input('Informe o CPF: ')
        dt_nascimento = input('Informe a data de nascimento: ')
        profissao = input('Informe a profissão: ')
        renda = float(input('Informe a renda: '))
        banco_clientes.setdefault(cpf, Cliente(nome, cpf, dt_nascimento, profissao, renda))

    elif op  == 3:#Conta corrente

        print('Informe os dados da conta corrente')
        cpf = input("CPF do Cliente: ")
        if cpf in banco_clientes.keys():
            numero = input("Numero da Conta")
            saldo = float(input('Informe o Saldo: '))
            limite = float(input('Informe o Limite: '))
            nome = input('Informe o nome: ')
            cpf = input('Informe o CPF: ')
            dt_nascimento = input('Informe a data de nascimento: ')
            profissao = input('Informe a profissão: ')
            renda = float(input('Informe a renda: '))

            banco_CC.setdefault(cpf, ContaCorrente(numero, saldo, limite, nome, cpf, dt_nascimento, profissao, renda))
        else:
            print("Cliente não existe!")
    elif op == 4:#Conta Poupança
        print('Informe os dados da conta poupança')
        cpf = input("CPF do Cliente: ")
        if cpf in banco_clientes.keys():
            numero = input("Numero da Conta")
            saldo = float(input('Informe o Saldo: '))
            limite = float(input('Informe o Limite: '))
            nome = input('Informe o nome: ')
            cpf = input('Informe o CPF: ')
            data_nascimento = input('Informe a data de nascimento: ')
            profissao = input('Informe a profissão: ')
            renda = float(input('Informe a renda: '))
            banco_CP.setdefault(cpf, ContaPoupanca(numero, saldo, limite, nome, cpf, dt_nascimento, profissao, renda))
        else:
            print("Cliente não existe!")
    elif op == 5:
        print('Informe os dados da Plano de Saude')
        cpf = input("CPF do Cliente: ")
        if cpf in banco_clientes.keys():
            valor_mensal = int(input('Informe o valor mensal: '))
            valor_total = int(input('Informe o valor total: '))
            nome = input('Informe o nome: ')
            cpf = input('Informe o CPF: ')
            dt_nascimento = input('Informe a data de nascimento: ')
            profissao = input('Informe a profissão: ')
            renda = float(input('Informe a renda: '))
            banco_SV.setdefault(cpf, SeguroDeVida(nome, cpf, dt_nascimento, profissao, renda, valor_mensal, valor_total))
        else:
            print("Cliente não existe!")
    elif op == 6:
        lista = []
        cpf = input("informe o cpf: ")
        if cpf in banco_CC.keys():
            lista.append(banco_CC.items())
            if cpf in banco_SV.keys():
                lista.append(banco_SV.items())
            total = CobrarTributacao.calculo_tributacao(lista, 1)
            for a in total:
                print(a)

    elif op == 7:
        
from conta import Conta
from cliente import Cliente
import datetime

class ContaPoupanca(Conta, Cliente):
    def __init__(self, numero, saldo, nome, cpf, dt_nascimento, profissao, renda):
        Conta.__init__(numero, saldo)
        Cliente.__init__(nome, cpf, dt_nascimento, profissao, renda)

    def deposita(self, valor):
        self.saldo += valor
        self._historico.append("Depósito de {} em {}".format(valor, datetime.datetime.today()))

    def sacar(self, valor):
        try:
            if self.saldo > 0:
                self.saldo -= valor
                self._historico.append("Saque de {} em {}".format(valor, datetime.datetime.today()))
        except:
            print("Saldo Insuficiente")

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.deposita(valor)
            print('Transferencia realizada com sucesso')
            return True
        else:
            print('Transferencia não pode ser realizada')
            return False

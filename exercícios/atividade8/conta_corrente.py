import datetime
from conta import Conta
from cliente import Cliente

class ContaCorrente(Conta, Cliente):
    def __init__(self, numero, saldo, limite, nome, cpf, dt_nascimento, profissao, renda):
        Conta.__init__(numero, saldo)
        Cliente.__init__(nome, cpf, dt_nascimento, profissao, renda)
        self._limite = limite


    def deposita(self, valor):
        self.saldo += valor - 0.10
        self._historico.append("Depósito de {} em {}".format(valor, datetime.datetime.today()))

    def sacar(self, valor):
        try:
            if self.saldo > 0:
                self.saldo -= valor
                self._historico.append("Saque de {} em {}".format(valor, datetime.datetime.today()))
                return True
        except:
            print("Saldo Insuficiente")
            return False

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.deposita(valor)
            print('Transferencia realizada com sucesso')
            return True
        else:
            print('Transferencia não pode ser realizada')
            return False

    def get_valor_imposto(self):
        return self.saldo - 0.01


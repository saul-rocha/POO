import abc
import datetime
from historico import Historico

class Conta(abc.ABC):

    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo
        self._historico = Historico()

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def historico(self):
        return self._historico

    @abc.abstractmethod
    def mostrar_historico_conta(self):
        pass

    @abc.abstractmethod
    def deposita(self):
        pass

    @abc.abstractmethod
    def sacar(self):
        pass

    @abc.abstractmethod
    def transferir(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, saldo, limite):
        super().__init__(numero, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def mostrar_historico_conta(self):
        self.historico.imprime()

    def deposita(self, valor):
        if(valor > 0):
            self.saldo += valor - 0.10
            self.historico.transacoes.append("Deposito de {} em {}".format(valor, datetime.datetime.today()))
            res = True
        else:
            res = False

        return res

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {} em {}".format(valor, datetime.datetime.today()))
            res = True
        else:
            res = False

        return res

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            self.historico.transacoes.append("Tranferência de {} para conta {} em {}".format(valor, destino.numero, datetime.datetime.today()))
            res = True
        else:
            res = False

        return res

    def get_valor_imposto(self):
        return self.saldo * 0.01


class ContaPoupanca(Conta):
    def __init__(self, numero, saldo):
        super().__init__(numero, saldo)


    def mostrar_historico_conta(self):
        self.historico.imprime()

    def deposita(self, valor):
        if (valor > 0):
            self.saldo += valor
            self.historico.transacoes.append("Deposito de {} em {}".format(valor, datetime.datetime.today()))
            res = True
        else:
            res = False

        return res

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {} em {}".format(valor, datetime.datetime.today()))
            res = True
        else:
            res = False

        return res

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            self.historico.transacoes.append("Tranferência de {} para conta {} em {}".format(valor, destino.numero, datetime.datetime.today()))
            res = True
        else:
            res = False
        return res



class SeguroDeVida():
    def __init__(self, valor_mensal, valor_total):
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total

    @property
    def valor_mensal(self):
        return self._valor_mensal

    @property
    def valor_total(self):
        return self._valor_total


    def get_valor_imposto(self):
        return 10 + self.valor_mensal * 0.02
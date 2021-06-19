import abc
from pessoa import Cliente
from historico import Historico

class Conta(abc.ABC, Cliente):
    def __init__(self, titular):
        Cliente.__init__(titular.pessoa, titular.profissao, titular.renda)
        self._historico = Historico()


    @property
    def titular(self):
        return self._titular

    @property
    def historico(self):
        return self._historico

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
    def __init__(self, titular, numero, saldo, limite):
        Conta.__init__(titular)
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self._tipo = "Conta Corrente"

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    def deposita(self, valor):
        if(valor > 0):
            self.saldo += valor - 0.10
            self.historico.transacoes.append("Deposito de {}".format(valor))
            res = True
        else:
            res = False

        return res

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            res = True
        else:
            res = False

        return res

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            self.historico.transacoes.append("Tranferência de {} para conta {}".format(valor, destino.numero))
            res = True
        else:
            res = False

        return res

    def get_valor_imposto(self):
        return self.saldo * 0.01


class ContaPoupanca(Conta):
    def __init__(self, titular, numero, saldo, limite):
        Conta.__init__(titular)
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self._tipo = "Conta Poupança"

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite


    def deposita(self, valor):
        if (valor > 0):
            self.saldo += valor
            res = True
        else:
            res = False

        return res

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            res = True
        else:
            res = False

        return res

    def trasnferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            self.historico.transacoes.append("Tranferência de {} para conta {}".format(valor, destino.numero))
            res = True
        else:
            res = False

        return res



class SeguroDeVida(Cliente):
    def __init__(self, titular, valor_mensal, valor_total):
        Cliente.__init__(titular)
        self._valor_mensal = valor_mensal
        self._valor_anual = valor_total

    @property
    def valor_mensal(self):
        return self._valor_mensal

    @property
    def valor_total(self):
        return self._valor_total


    def get_valor_imposto(self):
        return 10 + self.valor_mensal * 0.02
import abc
from manipulador_tributaveis import ManipuladorDeTributaveis
class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo, tipo, limite=1000.0, ):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @abc.abstractmethod
    def atualiza(self):
        pass


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo, "Poupança")

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0):
        super().__init__(numero, titular, saldo, "Corrente")

    def atualiza(self, taxa):
        self.saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self.saldo += valor - 0.10

    def get_valor_imposto(self):
        return self.saldo * 0.01


class SeguroDeVida:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if(isinstance(t, Tributavel)):
                total += t.get_valor_imposto()
            else:
                print(t.__repr__(), "não é um tributável")
        return total


if __name__ == '__main__':
    from tributavel import Tributavel
    cc = ContaCorrente('123-4', 'João')
    cc.deposita(1000.0)
    seguro = SeguroDeVida(100.0, 'José', '345-77')
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    lista_tributaveis = []
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)
    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    cp = ContaPoupanca('123-6', 'Maria', 400.00)
    lista_tributaveis.append(cp)
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)



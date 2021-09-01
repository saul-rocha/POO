import abc

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

#if __name__ == '__main__':
 #   c = Conta()
##Can't instantiate abstract class Conta with abstract methods atualiza

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo, "Poupança")

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo, "Corrente")

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        self._saldo += valor - 0.10

"""
if __name__ == '__main__':

    cc = ContaCorrente('123-5', 'Jose', float(1000.0))
    cp = ContaPoupanca('123-6', 'Maria', float(1000.0))


    cc.atualiza(0.01)
    cp.atualiza(0.01)


    print(cc.saldo)
    print(cp.saldo)

"""
class ContaInvestimento(Conta):

    def __init__(self, numero, titular, saldo):
        super(ContaInvestimento, self).__init__(numero, titular, saldo, "Investimento")

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def deposita(self, valor):
        self._saldo += valor - 0.10

if __name__ == '__main__':
    ci = ContaInvestimento('123-6', 'Maria', 1000)
    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print(ci.saldo)
    print(ci.tipo)
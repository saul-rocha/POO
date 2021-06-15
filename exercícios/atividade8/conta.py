import abc
from historico import Historico
##abstração da class Conta
class Conta(abc.ABC):
    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo
        self._historico = Historico()


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
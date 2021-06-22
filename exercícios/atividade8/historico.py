import datetime

class Historico:
    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    @property
    def data_abertura(self):
        return self._data_abertura

    @property
    def transacoes(self):
        return self._transacoes

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("HISTORICO DE ATIVIDADES")
        for t in self.transacoes:
            print(t)



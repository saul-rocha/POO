import datetime

class Historico:
    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self.transacoes = []

    @property
    def data_abertura(self):
        return self._data_abertura

    @property
    def transacoes(self):
        return self.transacoes()

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("TRANSAÇÕES")
        for t in self.transacoes:
            print(t, " - ")
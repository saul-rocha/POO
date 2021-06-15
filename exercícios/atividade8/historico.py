import datetime

class Historico:
    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    def imprimir_historico(self):
        print("Data de abertura: {}".format(self._data_abertura))
        print("Transações: ")
        for a in self._transacoes:
            print("-", a)
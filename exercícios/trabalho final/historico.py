import datetime

class Historico:
    def __init__(self):
        self._data_viagem = datetime.datetime.today()
        self._viagem = []

    @property
    def data_viagem(self):
        return self._data_viagem

    @property
    def viagem(self):
        return self._viagem

    def imprime(self):
        print("DATA DA VIAGEM: {}".format(self.data_abertura))
        print("HISTORICO DE VIAGENS")
        for t in self.viagem:
            print(t)
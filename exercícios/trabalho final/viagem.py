from historico import Historico
from sistema import Sistema

class Viagem:
    def __init__(self, local_saida, local_destino, cpf_motorista):
        self._local_saida = local_saida
        self._local_destino = local_destino
        self._motorista = cpf_motorista
        self._historico = Historico()

    @property
    def historico(self):
        return self._historico

    @property
    def motorista(self):
        return self._motorista

    @property
    def local_saida(self):
        return self._local_saida

    @property
    def local_destino(self):
        return self._local_destino

    def add_cliente(self, nome, valor):
        self.historico.viagem.append("Passageiro : {}\nLocal de Saída: {} \nLocal de Destino: {}\nValor: {}".format(nome, self.local_saida, self.local_destino, valor))

    def mostrar_viagem(self):
        self.historico.imprime()


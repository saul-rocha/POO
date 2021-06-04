class ControleBonificacao:

    def __init__(self):
        self._total_bonificacao = 0

    def registra(self, funcionario):
        self._total_bonificacao += funcionario.getBonificacao()


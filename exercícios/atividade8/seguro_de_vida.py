from cliente import Cliente

class SeguroDeVida(Cliente):
    def __init__(self, nome, cpf, dt_nascimento, profissao, renda, valor_mensal, valor_total):
        super().__init__(nome, cpf, dt_nascimento, profissao, renda)
        self._valor = valor_mensal
        self._valor_total = valor_total

    def get_valor_imposto(self):
        return 10 + (self._valor_mensal * 0.02)

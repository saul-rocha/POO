from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, profissao, renda):
        super().__init__(nome, cpf, dt_nascimento)
        self._profissao = profissao
        self._renda = renda

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @property
    def profissao(self):
        return self._profissao

    @property
    def renda(self):
        return self._renda
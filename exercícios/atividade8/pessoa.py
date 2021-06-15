class Pessoa:
    def __init__(self, nome, cpf, dt_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._dt_nascimento = dt_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def dt_nascimento(self):
        return self._dt_nascimento
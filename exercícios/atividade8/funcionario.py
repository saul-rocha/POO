from pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, salario):
        super().__init__(nome, cpf, dt_nascimento)
        self._salario = salario
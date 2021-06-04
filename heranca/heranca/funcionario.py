class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def getBonificacao(self):
        return self._salario*0.1

    def imprimir(self):
        print(self._nome, self._cpf)
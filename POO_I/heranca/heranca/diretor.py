from funcionario import Funcionario

class Diretor(Funcionario):

    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome,cpf, salario)
        self._senha = senha

    def getBonificacao(self):
        return self._salario*0.15

    def imprimirDiretor(self):
        super().imprimir()
        print(self._senha)
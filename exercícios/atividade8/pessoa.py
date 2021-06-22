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

    def mostrar_pessoa(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Data de Nascimento:", self.dt_nascimento)

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, salario):
        super().__init__(nome, cpf, dt_nascimento)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    def mostrar_funcionario(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Data de Nascimento:", self.dt_nascimento)
        print("Salario:", self.salario)


class Cliente(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, profissao, renda):
        super().__init__(nome, cpf, dt_nascimento)
        self._profissao = profissao
        self._renda = renda

    @property
    def profissao(self):
        return self._profissao

    @property
    def renda(self):
        return self._renda

    def mostrar_cliente(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Data de Nascimento:", self.dt_nascimento)
        print("Profissao:", self.profissao)
        print("Renda:", self.renda)


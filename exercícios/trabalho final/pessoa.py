from autentica import Autenticavel

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def cpf(self):
        return self._cpf


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)

class Motorista(Pessoa):
    def __init__(self, nome, idade, cpf, salario, nivel_cnh):
        super().__init__(nome, idade, cpf)
        self._salario = salario
        self._nivel_cnh = nivel_cnh

    @property
    def salario(self):
        return self._salario

    @property
    def nivel_cnh(self):
        return self._nivel_cnh

    def imprime(self):
        print("Nome: {}\nIdade: {}\nCPF: {}\nSalario: {}\nNivel CNH: {}".format(self.nome, self.idade, self.cpf, self.salario, self.nivel_cnh))


class Assistente(Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    def imprime(self):
        print("Nome: {}\nIdade: {}\nCPF: {}\nSalario: {}".format(self.nome, self.idade, self.cpf, self.salario))

class Gerente(Pessoa, Autenticavel):
    def __init__(self, nome, idade, cpf, login, senha):
        super().__init__(nome, idade, cpf)
        self._login = login
        self._senha = senha

    @property
    def login(self):
        return self._login

    @property
    def senha(self):
        return self._senha


    def autentica(self, login, senha):
        if login == self.login and senha == self.senha:
            return True
        else:
            return False
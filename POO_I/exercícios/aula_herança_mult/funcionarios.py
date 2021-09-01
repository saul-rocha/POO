import abc

class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

class Autenticavel:
    @abc.abstractmethod
    def autentica(self, senha):
        pass

# verifica se a senha confere

class Diretor(Funcionario, Autenticavel):

    def __init__(self, nome, cpf, salario, senha):
        super(Diretor, self).__init__(nome, cpf, salario)
        self._senha = senha

    def autentica(self, senha):
        return senha == self._senha
        # verifica se a senha confere

class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario, senha):
        super(Gerente, self).__init__(nome, cpf, salario)
        self._senha = senha

    def autentica(self, senha):
        return senha == self._senha
    # verifica se a senha confere e também se o seu departamento tem acesso


class Cliente(Autenticavel):
    def __init__(self,nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

    def autentica(self, senha):
        return self._senha == senha

class SistemaInterno:
    def __init__(self, gerente):
        self._gerente = gerente

    def login(self, obj, senha):

        if (hasattr(obj, 'autentica') and obj.autentica(senha)):
            print("{} AUTENTICADO!".format(obj.__class__.__name__))
            return True
            # chama método autentica
        else:
            print("{} NÃO AUTENTICADO!".format(obj.__class__.__name__))
            return False
            # imprime mensagem de ação inválida



g = Gerente("Saul", "0000000-0", 400.00, "12345")
c = Cliente("Manga", "111111-1", "54321")
d = Diretor("Flavio", "222222-2", 100000.00, "22222")
si = SistemaInterno()

si.login(g, "12345")
si.login(c, "12345")
si.login(d, "22222")
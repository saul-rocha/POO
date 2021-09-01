import datetime as dt

class Pessoa:
    #guarda apeenas o ano para que possa calcular a idade
    def __init__(self, nome, altura, dia, mes, ano):
        self._nome = nome
        self._ano = ano
        self._dt_nascimento = "{}/{}/{}".format(dia, mes, ano)
        self._altura = altura

###metodos gets
    @property
    def nome(self):
        return self._nome

    @property
    def dt_nasc(self):
        return self._dt_nascimento

    @property
    def altura(self):
        return self._altura

    @property
    def ano(self):
        return self._ano

###metods setts
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @dt_nasc.setter
    def dt_nasc(self, dt_nascimento):
        self._dt_nascimento = dt_nascimento

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @ano.setter
    def ano(self, ano):
        self._ano = ano

## imprimir todas as informações
    @property
    def imprimir(self):
        print("Nome:", self._nome)
        print("Data de Nascimento: ", self._dt_nascimento)
        print("Altura: ", self._altura)

## pega a data atual pela datatime e subtrai do ano em que a pessoa nasceu
    def idade(self):
        data_atual = dt.date.today()
        return data_atual.year - self._ano
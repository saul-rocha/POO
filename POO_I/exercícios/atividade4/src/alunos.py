class Alunos:

    def __init__(self, matricula, nome, n1, n2, n3):
        self._matricula = matricula
        self._nome = nome
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3

    @property
    def matricula(self):
        return self._nome

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def n1(self):
        return self._n1

    @property
    def n2(self):
        return self._n2

    @property
    def n3(self):
        return self._n3

    def media(self):
        return ((self._n1 * 2) + (self._n2 * 3) + (self._n3 * 5)) / (2 + 3 + 5)

    def final(self):

        if(self.media() >= 4 and self.media() < 7):
            res = (14 - self.media())
        else:
            res = 0

        return res



import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data de abertura: {}".format(self.data_abertura))
        print("transações: ")
        for i in self.transacoes:
            print("-", i)

class Client:
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
##SET
    def setNome(self):
        return self._nome

    def setSobrenome(self):
        return self._sobrenome

    def setCpf(self):
        return self._cpf
##GET
    def getNome(self, nome):
        self._nome = nome

    def getSobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    def getCpf(self, cpf):
        self._cpf = cpf


    def imprimir(self):
        print("nome: ", self._nome)
        print("sobrenome: ", self._sobrenome)
        print("cpf: ", self._cpf)


class Conta:

    def __init__(self, numero, Client, saldo = 0, limite = 100):
        self._numero = numero
        self._titular = Client
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
##retorna True se foi efetuado e False caso não
    def deposita(self, valor):
        if valor < 0:
            return False
        else:
            self.saldo += valor
            self.historico.transacoes.append("Deposito  de {}".format(valor))
            return True

    def saca(self, saque):
        if self.saldo > saque:
            self.saldo -= saque
            self.historico.transacoes.append("Saque  de {}".format(saque))
            return True
        else:
            return False

    def extrato(self):
        print("Numero da Conta:", self.numero)
        self.titular.imprimir()
        print("Saldo: ", self.saldo)
        print("Limite: ", self.limite)
        self.historico.imprime()
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transferencia(self, destino, valor):
        if valor < 0:
            return False
        elif self.saldo >= valor:
            retira = self.saca(valor)
            if (retira == False):
                return False
            else:
                destino.deposita(valor)
                self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
                return True
        else:
            return False
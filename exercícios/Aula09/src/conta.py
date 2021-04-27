class Conta:

    def __init__(self, numero, titular, saldo = 0, limite = 100):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
##retorna True se foi efetuado e False caso não
    def deposita(self, valor):
        if valor < 0:
            return False
        else:
            self.saldo += valor
            return True

    def saca(self, saque):
        if self.saldo > saque:
            self.saldo -= saque
            return True
        else:
            return False

    def extrato(self):
        print("Numero: {}\nTitular: {}\nSaldo: {}\nLimite: {}".format(self.numero, self.titular, self.saldo, self.limite))

class Sistema:

    def __init__(self):
        self._motoristas = {}
        self._assistentes = {}
        self._viagens = {}
        self._historico_viagens = []


    @property
    def motoristas(self):
        return self._motoristas


    @property
    def assistentes(self):
        return self._assistentes

    @property
    def historico_viagens(self):
        return self._historico_viagens
    @property
    def viagens(self):
        return self._viagens

    def add_motorista(self, motorista):
        if motorista.cpf in self.motoristas.keys():
            return False
        else:
            self.motoristas[motorista.cpf] = motorista
            return True

    def add_assistente(self, assistente):
        if assistente.cpf in self.assistentes.keys():
            return False
        else:
            self.assistentes[assistente.cpf] = assistente
            return True

    def fazer_viagem(self, v, id_viagem):
        self.viagens[id_viagem] = v

    def consultar_funcionarios(self):
        for key, motorista in self.motoristas.items():
            print("__________________________")
            motorista.imprime()
            print("__________________________")

        for key, assistente in self.assistentes.items():
            print("__________________________")
            assistente.imprime()
            print("__________________________")

    def mostrar_viagens(self):
        for key, viagem in self.viagens.items():
            viagem.mostrar_viagem()
            print("---------------------------------------------")

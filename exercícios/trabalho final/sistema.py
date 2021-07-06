class Sistema:
    def __init__(self):
        self._motoristas = {}
        self._assistentes = {}
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

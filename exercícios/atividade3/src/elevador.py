class Elevador:
    
    def __init__(self, total_andares, capacidade):
        self._andar_atual = 0
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._qtdpessoa = 0
    

    
    def entra(self):
        if self._capacidade > self._qtdpessoa:
            self._qtdpessoa += 1
            return True
        else:
            return False
    
    def sai(self):
        if self._qtdpessoa > 0:
            self._qtdpessoa -= 1
            return True
        else:
            return False
    
    def sobe(self):
        if self._andar_atual < self._total_andares:
            self._andar_atual += 1
            return True
        else:
            return False
    
    def desce(self):
        if self._andar_atual != 0:
            self._andar_atual -= 1
            return True
        else:
            return False

### Getters
    @property
    def andar_atual(self):
        return self._andar_atual
    
    @property
    def total_andares(self):
        return self._total_andares
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @property
    def qtdpessoa(self):
        return self._qtdpessoa

### Setters
    @andar_atual.setter
    def andar_atual(self, andar):
        self._andar_atual = andar
    
    @total_andares.setter
    def total_andares(self, total):
        self._total_andares = total
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self._capacidade = capacidade
    
    @qtdpessoa.setter
    def qtdpessoa(self, qtdpessoas):
        self._qtdpessoa = qtdpessoas

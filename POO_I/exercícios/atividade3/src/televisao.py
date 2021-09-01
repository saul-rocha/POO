class Televisao:
    def __init__(self, volume=0, canal=0):
        self._volume = volume
        self._canal = canal


class ControleRemoto:
    def __init__(self, televisao):
        self.televisão = televisao
    
    def opcoes(self):
        print("1- Aumentar Volume")
        print("2- Diminuir Volume")
        print("3- Proximo Canal")
        print("4- Canal Anterior")
        print("5- Consulta Canal")
        print("6- Consulta Volume")
        print("0- Desligar")

        op = int(input("Escolha: "))
        return op
    
    
    def aumentar_volume(self):
        if(self.televisão._volume < 100):
            self.televisão._volume += 1
            return True
        else:
            return False
    
    def diminuir_volume(self):
        if self.televisão._volume > 0:
            self.televisão._volume -= 1
            return True
        else:
            return False
    
    def prox_canal(self):
        self.televisão._canal += 1
        return True
    
    def ante_canal(self):
        self.televisão._canal -= 1
        return True
    
    @property
    def consulta_volume(self):
        return self.televisão._volume
    
    @property
    def consulta_canal(self):
        return self.televisão._canal
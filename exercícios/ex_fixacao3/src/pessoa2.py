

class Agenda:
    def __init__(self):
        self.agenda = []
        self.tam = 10
    ### se a agenda não estiver cheia adiciona uma pessoa no final da lista

    def armazenaPessoa(self, nome, idade, altura):
        if len(self.agenda) < self.tam:
            pessoa = (nome, idade, altura)
            self.agenda.append(pessoa)
            return 1 ##retona 1 se tiver ok
        else:
            return 0 ## retorna 0 se não ffor adicionado(lista cheia)
    ### percorre a lista e verifica se o nome está contido na pessoa daquela posição
    def removePessoa(self, nome):
        for a in self.agenda:
            if nome in a:
                self.agenda.remove(a)
                return 1 #retorna 1 se for removido
        return 0 ##retorna 0 se não encontrar a pessoa

    def buscaPessoa(self, nome):
        for a in self.agenda:
            if nome in a:
                return self.agenda.index(a)
        return 0

    def imprimeAgenda(self):
        for a in self.agenda:
            print("Nome: ", a[0])
            print("Idade: ", a[1])
            print("Altura: ", a[2])
            print("-----------------")

    def imprimePessoa(self, index):
        print("Nome: ", self.agenda[index][0])
        print("Idade: ", self.agenda[index][1])
        print("Altura: ", self.agenda[index][2])



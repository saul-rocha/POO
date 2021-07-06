class Subscriber:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def atualiza(self, mensagem):
        print("{} '{}'".format(self.nome, mensagem))


class Publisher:
    def __init__(self, eventos):
        self._subcribers = {evento: dict() for evento in eventos}


    def get_subscribers(self, evento):
        return self._subcribers[evento]

    def registrar(self, evento, nome, callback = None):
        if callback is None:
            #O método getattr () retorna o valor do atributo nomeado de um objeto.
            # Se não for encontrado, ele retorna o valor padrão fornecido para a função.
            callback = getattr(nome, 'atualiza')

        self.get_subscribers(evento)[nome] = callback


    def despacho(self, evento, menssagem):
        for subscriber, retorno in self.get_subscribers(evento).items():
            retorno(menssagem)



import abc


class Autenticavel(abc.ABC):
    """ Classe que contém operações de um objeto autenticável
        As subclasses concretas devem sobrescrever o método autenticavel.
        """
    @abc.abstractmethod
    def autentica(self, login, senha):
        """ torna um objeto autenticável """
        pass
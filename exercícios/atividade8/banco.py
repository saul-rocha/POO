from manipulador_tributaveis import ManipuladorDeTributaveis

class Banco:
    def __init__(self):
        self._lista_funcionarios = {}
        self._lista_clientes = {}
        self._lista_contas_correntes = {}
        self._lista_contas_poupancas = {}
        self._lista_seguros_de_vida = {}
        self._lista_historico_tributacoes = []

    @property
    def lista_funcionarios(self):
        return self._lista_funcionarios

    @property
    def lista_clientes(self):
        return self._lista_clientes

    @property
    def lista_contas_correntes(self):
        return self._lista_contas_correntes

    @property
    def lista_contas_poupancas(self):
        return self._lista_contas_poupancas

    @property
    def lista_seguros_de_vida(self):
        return self._lista_seguros_de_vida

    @property
    def lista_historico_tributacoes(self):
        return self._lista_historico_tributacoes


    def get_cliente(self, cpf):
        return self._lista_clientes.get(cpf)

    def mostrar_clientes(self):
        for key, cliente in self._lista_clientes.items():
            print("----------------------")
            cliente.mostrar_cliente()
            print("----------------------")

    def adicionar_funcionario(self, funcionario):
        self._lista_funcionarios[funcionario.cpf] = funcionario

    def adicionar_cliente(self, cliente):
        self._lista_funcionarios[cliente.cpf] = cliente

    def adicionar_conta_corrente(self, cc):
        self._lista_funcionarios[cc.cliente.cpf] = cc

    def adicionar_conta_poupanca(self, cp):
        self._lista_funcionarios[cp.cliente.cpf] = cp

    def adicionar_seguro_de_vida(self, sv):
        self._lista_seguros_de_vida[sv.cliente.cpf] = sv

    def calcular_tributos(self):
        self._lista_historico_tributacoes

    def sacar(self, conta, valor):
        res = conta.sacar(valor)
        return res


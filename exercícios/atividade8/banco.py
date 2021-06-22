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



    def adicionar_funcionario(self, funcionario):
        if funcionario.cpf in self.lista_funcionarios.keys():
            return False
        else:
            self.lista_funcionarios[funcionario.cpf] = funcionario
            return True

    def adicionar_cliente(self, cliente):
        if cliente.cpf in self.lista_clientes.keys():
            return False
        else:
            self.lista_clientes[cliente.cpf] = cliente
            return True

    def adicionar_conta_corrente(self, cpf, cc):
        if cpf in self.lista_contas_correntes.keys():
            return False
        else:
            self.lista_contas_correntes[cpf] = cc
            return True
    def adicionar_conta_poupanca(self, cpf, cp):
        if cpf in self.lista_contas_poupancas.keys():
            return False
        else:
            self.lista_contas_poupancas[cpf] = cp
            return True
    def adicionar_seguro_de_vida(self, cpf, sv):
        if cpf in self.lista_seguros_de_vida.keys():
            return False
        else:
            self.lista_seguros_de_vida[cpf] = sv
            return True

    def imprimir_banco(self):
        print("CLIENTES")
        for key, cliente in self.lista_clientes.items():
            cliente.mostrar_cliente()
        print("FUNCIONARIOS")
        for key, funcionario in self.lista_funcionarios.items():
            funcionario.mostrar_funcionario()
        print("CONTAS POUPANÇAS")
        for key, cp in self.lista_contas_poupancas.items():
            print(cp)
        print("CONTAS CORRENTE")
        for key, cc in self.lista_contas_correntes.items():
            print(cc)
        print("SEGUROS")
        for key, sv in self.lista_seguros_de_vida.items():
            print(sv)


    def mostrar_historico_contap(self, cpf):
        self.lista_contas_poupancas[cpf].mostrar_historico_conta()

    def mostrar_historico_contac(self, cpf):
        self.lista_contas_correntes[cpf].mostrar_historico_conta()

    def calcular_tributos(self, lista_tributaveis, trib):
        mt = ManipuladorDeTributaveis
        total = mt.calcula_impostos(self,lista_tributaveis)
        self.lista_historico_tributacoes.append("{} Tributação = R$ {}".format(trib, total))
        return trib + 1

    def imprimir_historico_tributacoes(self):
        for a in self.lista_historico_tributacoes:
            print(a)



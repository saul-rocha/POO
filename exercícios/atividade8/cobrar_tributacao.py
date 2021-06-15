from tributavel import Tributavel

class CobrarTributacao:

    def calculo_tributacao(self, lista_tributaveis, qtd):
        total = []
        trib = 0
        for t in lista_tributaveis:
            if(isinstance(t, Tributavel)):# se tiver um metodo da classe tributavel
                trib += t.get_valor_imposto()
                total.append("{} tributação = {}".format(qtd, trib))
                qtd += 1
            else:
                print(t.__repr__(), "não é um tributável")
        return total
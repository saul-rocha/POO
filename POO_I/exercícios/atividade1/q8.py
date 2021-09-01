# espetaculo = 200$
# ingresso = 5$
# qtd = 120

# valores iniciais
esp = 200
ingress = 5.00
qtd = 120
lucro = (ingress * qtd) - esp

#melhor resultado inicial
lmax = lucro
pmax = ingress
qtdmax = qtd

#condição de parada
while ingress >= 1.5:
    print("preço do ingresso = {}, quantidade = {}, lucro = {}".format(ingress,qtd,lucro))
    ingress -= 0.5
    qtd += 26
    lucro = (ingress * qtd) - esp

    if(lucro > lmax):
        lmax = lucro
        pmax = ingress
        qtdmax = qtd

print("\n\n")
print("lucro maximo = ", lmax)
print("preço do ingresso = ", pmax)
print("quantidad vendida = ", qtd)
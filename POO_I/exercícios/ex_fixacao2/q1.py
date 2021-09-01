modelo = ['FUSCA', 'GOL', 'UNO', 'VECTRA', 'PEUGOUT']
kmlitro = [7.0, 10, 12.5, 9, 14.5]

km = kmlitro[0] #mais econômico is the first of elements the list
id = 0

#range begin 1 e recebe como parametro o tamanho da lista
for a in range(1, len(kmlitro)):#percorre todos os indices da lista e devolve o indice que tem o modelo de menor consumo
    if kmlitro[a] > km:
        km = kmlitro[a] #qundo encontrar um que seja mais economic, substitui o anterior pelo atual
        id = a # e o id do veículo agora


# L/1000KM
print("Relatório Final")
for x in range(len(modelo)):
    litros = 1000 / kmlitro[x] # quantos litros gasta para percorrer 1000km
    valor = litros * 2.24 # valor gasto com o combustível para percorrer 1000km

    print("{} - {}      - {} KM/L - {:.1f} litros - R$ {:.2f}".format(x, modelo[x], kmlitro[x], litros, valor))


print("Modelo mais econômico\nVeículo {}\nNome: {}\n{} KM/L".format(id, modelo[id], kmlitro[id]))
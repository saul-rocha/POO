def imprimeLista(lista): #recebe um lista como parametro
    for a in lista: # percorre a lista
        if isinstance(a, list): # se o elemento for uma lista
            imprimeLista(a) # chama recursivamente passando o elemendo da lista principal e imprime-a
        else:
            print(a) # imprime o elemento da lista

lista = [1, 2.5, "a", True]

imprimeLista(lista)
def meu_find(search,lista): # tem como parametros o elemento que deseja buscar e a lista
    cont = 0 # pega a posição do elemento. começa de zero
    for a in lista: # percorre a lista
        if search == a: # se o elemento que esta procurando for igual ao da lista
            return cont # retorna sua posição
        else:
            cont += 1 # caso contrario cont é iterado para a proxima posição

index = meu_find("T","Teste")
print(index)
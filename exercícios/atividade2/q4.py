def ordenar_lista(string):
    #converte a string em lista
    lista = list(string)
    # obtém o tamanho da lista
    len_lista = len(lista)
# loop mais externo começando de (len_lista - 1) até 1 com decremento -1
    for i in range(len_lista - 1, 0, -1):
    # for mais interno que vai de 0 até (i - 1)
        for j in range(i):
        # o "if" testa se a string acessada pelo índice (j + 1)
        # precede a string acessada pelo índice "j"
            if(lista[j] > lista[j + 1]):
                # faz a troca dos elementos
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    res = ''.join(lista) #transforma a lista em string
    return res # retorna a string ordenada

lista = "saul"
# chama a função ordenar_lista
res = ordenar_lista(lista)
# imprime a lista ordenada alfabeticamente
print(res)
def primo(num):
    cont = 0 # cont irá contar quantos valores num é divisivel
    aux = 1 # irá ser incrementada até que seja igual a num
    while(aux <= num): # condição de encerramento da repetição
        if num % aux == 0:# verifica se num é divisivel por aux
            cont += 1 # se sim, cont é incrementada
        aux +=1 

    if cont <= 2:
        return True # se cont for menor ou igual a 2 é porque o numero é divisivel por 1  epor ele mesmo e é primo
    else:
        return False # caso nao se ja primo

## leitura dos valores
n1 = int(input("digite um umero: "))
n2 = int(input("digite um numero: "))

cont = 0# irá contar a quantidade de primos

if(n1 > 0 and n2 > 0): # condição para entrada
    if(n1 >= n2):# verifica qual o maior
        for x in range(n2,n1+1):# percorre o intervalo entre n1 e n2 do menor para o meior
            if primo(x) == True:
                print(x)
                cont +=1
        if(cont < 1):
            print("Não existe nenhum número primo dentro desse intervalo") # caso nao tenha memhu, primo no intervalo
    elif(n1 <= n2): # idem anterior
        for x in range(n1,n2+1):
            if primo(x) == True:
                print(x)
                cont += 1
        if(cont < 1):# caso nao tenha memhu, primo no intervalo
            print("Não existe nenhum número primo dentro desse intervalo")
else:
    print("digite um numero inteiro e positivo")
pessoas = []

for a in range (10):
    aux = []
    nome = input("Nome: ")
    add = input("Endereço: ")
    cep = int(input("CEP: "))
    bairro = input("Bairro: ")
    tel = int(input("Telefone: "))

    aux.append(nome)
    aux.append(add)
    aux.append(cep)
    aux.append(bairro)
    aux.append(tel)

    pessoas.append(aux)

print(pessoas)

print("dados invertidos")
for x in range(10):
    aux = []
    aux = pessoas[x]
    aux.reverse()
    print(aux)

# resta inverter os itens



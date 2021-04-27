from src.conta import Conta # importa a classe do diretorio src

c = Conta("Saul", "123")
c1 = Conta("Flavio", "321", 1000)

print(c1.saldo)

res = c1.saca(10)

if res == True:
    print("OK!")
else:
    print("Nao realizado")

c1.extrato()
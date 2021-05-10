from src.conta import Conta, Client # importa a classe do diretorio src

cc = Client("Saul", "Rocha", "1111")
c1c = Client("Flavio", "Henrique", "2222")
c = Conta("123", cc, 300)
c1 = Conta("321", c1c, 1000)

print(c.saldo)
res = True
#res = c1.saca(10)

if res == True:
    print("OK!")
else:
    print("Nao realizado!")

res = c.transferencia(c1, 200)
if res == True:
    print("OK!")
else:
    print("Nao realizado!")

c.deposita(200)


c.extrato()
print("\n")
c1.extrato()
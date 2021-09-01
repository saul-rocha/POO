salario = float(input("Quanto voce ganha por hora? "))
horas = int(input("Quantas horas de trabalho por mês? "))

bruto = salario * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05

liquid = bruto - ir - inss - sindicato

print("salario bruto: {}".format(bruto))
print("IR: {}".format(ir))
print("INSS: {}".format(inss))
print("Sindicato: {}".format(sindicato))
print("Salario Liquido: {}".format(liquid))
"""
Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro
Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro
"""

litros = float(input("litros vendidos: "))
tipo = input("A - Alcool\nG - Gasolina\nEscolha: ")

if tipo == 'a' or tipo == 'A':
    #se menor que 20L o desconto é de 3% por litro
    if litros < 20:
        valor = (litros * (3.45 - (3.45*0.03)))
        print("Valor = {:.2f} R$".format(valor))
    # se maior que 20L desconto é de 5%    
    else:
        valor = (litros * (3.45 - (3.45*0.05)))
        print(("Valor = {:.2f} R$").format(valor))
elif tipo == 'g' or tipo == 'G':
    #se menor que 20L deconto = 4%
    if litros < 20:
        valor = (litros * (4.53 - (4.53*0.04)))
        print("Valor = {:.2f} R$".format(valor))
    #se menor que 20L deconto = 6%
    else:
        valor = (litros * (4.53 - (4.53*0.06)))
        print(("Valor = {:.2f} R$").format(valor))
else:
    print("Tipo de combustivel nao existe")
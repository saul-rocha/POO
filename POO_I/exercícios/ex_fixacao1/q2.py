#leitura do peso 
peso = float(input("Peso de peixes: "))
#excesso de peso (acima de 50 há multa)
excesso = peso - 50
if (excesso > 0):
    #valor da multa caso tenha execedido o peso de 50kg em peixes
    multa = excesso * 4
    print("peso excedido {} KG: " .format(excesso))
    print("multa = {:.1f} R$".format(multa))
else:
    print("Não há excesso")

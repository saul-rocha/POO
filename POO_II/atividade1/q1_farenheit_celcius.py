"""
1 - Faça um Programa que peça a temperatura em graus Farenheit, transforme 
    e mostre a temperatura em graus Celsius: 
                    C = (5 * (F-32) / 9).
""" 

#leitura do valor em F
f = int(input("Temperatura em Farenheit: "))
#conversão de Farenheit para Celsius
c = (5*((f-32)/9))
#saída
print("{}°F equivale a {:.1f}°C".format(f,c))
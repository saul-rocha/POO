lado_a = int(input("lado A: "))
lado_b = int(input("lado B: "))
lado_c = int(input("lado C: "))

if lado_b > lado_a:
    aux = lado_a
    lado_a = lado_b
    lado_b = aux
if lado_c > lado_a:
    aux = lado_a
    lado_a = lado_c
    lado_c = aux

if lado_a >= lado_b + lado_c:
    print("NAO FORMA TRIANGULO")
else:
    if lado_a * lado_a == (lado_b * lado_b) + (lado_c * lado_c):
        print("TRIANGULO RETANGULO")
    elif (lado_a * lado_a) > (lado_b * lado_b) + (lado_c * lado_c):
        print("TRIANGULO OBTUSANGULO")
    elif (lado_a * lado_a) < (lado_b * lado_b) + (lado_c * lado_c):
        print("TRIANGULO ACUTANGULO")
    if (lado_a == lado_b) and (lado_b == lado_c):
        print("TRIANGULO EQUILATERO")
    elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
        print("TRIANGULO ISOSCELES")
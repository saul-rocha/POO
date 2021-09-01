l1 = input("lado 1: ")
l2 = input("lado 2: ")
l3 = input("lado 3: ")


if l1 > (l2+l3) or l2 > (l1+l3) or l3 >(l2+l1):
    print("Nao forma triangulo")
elif l1 == l2 and l1 == l3:
    print("Equilátero")
elif l1 != l2 and l2 != l3 and l1 != l3:
    print("Escaleno")
else:
    print("Isoceles")
    
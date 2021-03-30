n = int(input("montar tabuada de: "))
i = int(input("começa por: "))
f = int(input("termina em: "))

print("vou montar a tabuada de 5 começando em 4 e terminando em 7:")
for x in range(i,f+1):
    print("{} * {} = {}".format(n,x,n*x))
   

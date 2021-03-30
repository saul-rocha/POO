fib = int(input("quantos termos? "))

t1 = 0
t2 = 1
t3 = 0

while t3 <= fib:
    print("{} ".format(t3))
    t3 = t1 + t2
    t1 = t2
    t2 = t3
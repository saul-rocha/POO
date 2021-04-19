dic = {111: ["saul", 22], 222: ["jaca", 21], 333: ["menor", 17]}

maiores = [x[0] for n, x in dic.items() if x[1] > 18]

print(maiores)


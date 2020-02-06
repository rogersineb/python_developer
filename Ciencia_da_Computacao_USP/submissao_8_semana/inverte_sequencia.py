numero = [-1]

while numero[-1] != 0:
    numero.append(int(input("Digite um número: ")))

del numero[0]
del numero[-1]

for x in range(len(numero)-1, -1, -1):
    print(numero[x])


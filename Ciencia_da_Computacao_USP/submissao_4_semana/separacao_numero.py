numero = int(input("Digite o número: "))
aux = str(numero)
soma = 0
i = 0

while i < len(aux):
    soma += numero % 10
    numero = numero // 10
    i += 1
print(soma)
numero = int(input("Digite um número inteiro: "))
contador = 0
i = 1
while i <= numero:
    if(numero % i == 0):
        contador += 1
    i += 1
if contador == 2:
    print("primo")
else:
    print("não primo")
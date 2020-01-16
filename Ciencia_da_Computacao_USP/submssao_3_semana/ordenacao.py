primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
terceiroNumero = int(input("Digite o terceiro número: "))

if primeiroNumero < segundoNumero and segundoNumero < terceiroNumero:
    print("crescente")
else:
    print("não está em ordem crescente")
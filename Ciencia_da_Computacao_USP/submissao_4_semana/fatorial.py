numero = int(input("Digite o valor de n: "))
fatorial = numero
if numero == 0:
    print(1)
else:
    while numero > 1:
        fatorial =  fatorial * (numero - 1)
        numero = numero - 1
    print(fatorial) 
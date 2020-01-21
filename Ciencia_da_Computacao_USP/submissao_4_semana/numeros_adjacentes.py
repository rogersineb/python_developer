numero = int(input("Digite o número: "))
aux = str(numero)
haAdjacente = False
i = 0
if(len(aux) > 1):
    while i < len(aux):
        ultimoDigito = numero % 10
        numero = numero // 10
        if ultimoDigito == (numero % 10):
            haAdjacente = True
        i += 1
    if haAdjacente:
        print("sim")
    else:
        print("não")
else:
    print("não")

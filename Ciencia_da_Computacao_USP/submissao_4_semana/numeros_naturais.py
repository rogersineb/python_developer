numero = int(input("Digite o valor de n: "))
numeroNatural = 1
i = 0

while i < numero:
    if(numeroNatural % 2 != 0):
        print(numeroNatural)
        i += 1
    numeroNatural += 1
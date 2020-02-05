largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

i = 0
while i < altura:
    j = 0
    while j < largura:
        print("#", end="")
        j += 1
    i += 1
    print()

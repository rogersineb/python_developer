largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

i = 0
while i < altura:
    j = 0
    while j < largura:
        if i == 0 or i == altura-1:
            print("#", end="")
        else:
            if j == 0 or j == largura-1:
                print("#", end="")
            if j!= 0 and j != largura-1:
                print(end=" ")
        j += 1
    i += 1
    print()

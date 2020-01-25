def maior_primo(numero):
    i = 2
    maior_primo = 2
    while i <= numero:
        cont = 0
        j = 1
        while j <= i:
            if i % j == 0:
                cont += 1
            j += 1
        if cont == 2:
            maior_primo = i
        i += 1
    return maior_primo

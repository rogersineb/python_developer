def insertion_sort(lista):

    fim = len(lista)

    for i in range(fim -1):
        #Inicialment, o menor elemento já visto é o i-ésimo
        posicao_do_minimo = i

        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j

        #Colcoa o menor elemento encontrado no início da sub-lista
        #Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    return lista

class Ordenador:
    def selecao_direta(self, lista):
        
        fim = len(lista)

        for i in range(fim -1):
            #Inicialment, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
                    return True
            #Colcoa o menor elemento encontrado no início da sub-lista
            #Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

def ordenada(lista):
    ordenador = Ordenador()
    if ordenador.selecao_direta(lista):
        return False
    else:
        return True

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

def test_ordena():
    assert ordenada([10, 3, 8, -10, 200, 17, 32]) == False

def test_busca():
    assert busca(['a', 'e', 'i'], 'e') == 1

def test_busca_():
    assert busca([12, 13, 14], 15) == False
    

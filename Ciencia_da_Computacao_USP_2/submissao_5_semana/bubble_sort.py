def bolha_curta(lista):
        
    fim = len(lista)

    for i in range(fim-1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
                print(lista)
        if not trocou:
            return


def bubble_sort(lista):
    bolha_curta(lista)
    return lista

def test_bubble_sort():
    assert bubble_sort([5, 1, 4, 2]) == [1, 2, 4, 5]

def test_dimensao():
    assert dimensoes([[1],[2],[3]]) == "3X1"

def test_dimensao_2():
    assert dimensoes([[1,2,3], [4,5,6]]) == "2X3"

def dimensoes(matriz):
    linha = len(matriz)
    colunas = len(matriz[0])

    print(str(linha)+"X"+str(colunas))


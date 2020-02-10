def test_soma_matrizes():
    assert soma_matrizes([[1,2,3],[4,5,6]],[[2,3,4],[5,6,7]]) == [[3,5,7],[9,11,13]]

def test_soma_matrizes_false():
    assert soma_matrizes([[1],[2],[3]],[[2,3,4],[5,6,7]]) == False

def test_soma_matrizes_2x2_3x3():
    assert soma_matrizes([[5,6],[12,2]],[[1,2,3],[1,2,3]]) == False

def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        soma = []
        for numero_linha in range(len(m1)):
            soma.append([])
            for numero_coluna in range(len(m1[0])):
                soma[numero_linha].append(m1[numero_linha][numero_coluna] + m2[numero_linha][numero_coluna])
        return soma
    else:
        return False

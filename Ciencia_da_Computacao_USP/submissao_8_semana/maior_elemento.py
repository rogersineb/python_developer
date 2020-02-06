def maior_elemento(lista):
    lista.sort()
    return lista[-1]

def test_maior():
    assert maior_elemento([5,9,8,6,14,20,7,9,2]) == 20

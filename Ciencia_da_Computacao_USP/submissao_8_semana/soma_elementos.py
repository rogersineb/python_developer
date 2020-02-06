def soma_elementos(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma


def test_soma():
    assert soma_elementos([5,3,2,5,3,2,5,3,2]) == 30

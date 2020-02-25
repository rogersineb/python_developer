def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        soma = lista[-1] + soma_lista(lista[:len(lista)-1])
        return soma
'''
import pytest

@pytest.mark.parametrize("entrada, esperado", [
    ([0,2,3,8,9,10,20,-20],32),
    ([1, -5, -4, -20], -28),
    ([1.0, 0.0, 10.6, 4.8, 7.6],24),
    ([3, 8, 10, -5], 16)
    ])
def test_soma(entrada, esperado):
    assert soma_lista(entrada) == esperado
'''

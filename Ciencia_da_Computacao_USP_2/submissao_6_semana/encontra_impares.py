def encontra_impares(lista):
    if len(lista) >= 1:
        numero = [lista.pop(0)]
        encontra_impares(lista)
        if numero[0] % 2 != 0:
            lista.extend(numero)
    else:
        return      
    return lista
'''
import pytest

@pytest.mark.parametrize("entrada, esperado",[
    ([0, 2, 8, 4, 9, 12, 11, 74, 35], [35, 11, 9]),
    ([2, 4, 6, 8, 12, 14, 20, 22, 18], []),
    ([0], []),
    ([3, 5, 11], [11, 5, 3])
    ])

def testa_impares(entrada, esperado):
    assert encontra_impares(entrada) == esperado
'''

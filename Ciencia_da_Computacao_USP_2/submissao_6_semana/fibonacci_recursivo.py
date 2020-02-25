def fibonacci(numero):
    if numero < 2:                      # base da recursão
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2) #chamada recursiva


import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0 , 0),
    (1 , 1),
    (2 , 1),
    (3 , 2),
    (4 , 3),
    (5 , 5),
    (6 , 8),
    (7 , 13)
    ])
def test_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado
    

import sys

def fatorial(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        while numero > 1:
            fatorial =  fatorial * numero
            numero = numero - 1
        return fatorial

def coeficienteBinomial(numero, classe):
    print(fatorial(numero)/(fatorial(classe)*fatorial(numero - classe))) 

def test_fatorial0():
    assert fatorial(0) == 1
def test_fatorial1():
    assert fatorial(1) == 1
def test_fatorial_negativo():
    assert fatorial(-10) == 0
def test_fatorial4():
    assert fatorial(4) == 24
def test_fatorial5():
    assert fatorial(5) == 120


coeficienteBinomial(6, 3)
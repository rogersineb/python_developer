def maiusculas(frase):
    maiusculas =[]
    nova_string = ""
    for i in range(len(frase)):
        if ord(frase[i]) > 64 and ord(frase[i]) <=  90:
            nova_string += frase[i]

    return nova_string

def test_maiusculas():
    assert maiusculas('Programamos em python 2?') == 'P'

def test_maiuscula_1():
    assert maiusculas('Programamos e Python 3.') == 'PP'

def test_maiuscula_2():
    assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'

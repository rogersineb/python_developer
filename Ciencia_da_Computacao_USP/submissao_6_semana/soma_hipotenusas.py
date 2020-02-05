def é_hipotenusa(numero):
    i = 1
    while i < numero:
        j = 1
        while j < numero:
            if numero**2 == i**2 + j**2:
                return True
            j += 1
        i += 1
    
def soma_hipotenusas(limite):
    soma = 0
    i = 1
    while i <= limite:
        if é_hipotenusa(i):
            soma += i
        i += 1
    return soma

  

def test_answer_5():
    assert é_hipotenusa(5) == True

def test_answer_10():
    assert é_hipotenusa(10) == True

def test_answer_13():
    assert é_hipotenusa(13) == True

def test_answer_15():
    assert é_hipotenusa(15) == True

def test_answer_17():
    assert é_hipotenusa(17) == True

def test_answer_20():
    assert é_hipotenusa(20) == True

def test_answer_25():
    assert é_hipotenusa(25) == True

def test_answer():
    assert soma_hipotenusas(25) == 105

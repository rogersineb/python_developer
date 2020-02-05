def e_primo(n):
    i = 2
    while i <= n/2:
        if n % i == 0:
            return False
        i += 1
    return True


def n_primos(numero):
    cont = 0
    i = 2
    while i <= numero:
        if e_primo(i):
            cont += 1
        i += 1
    return cont
        

def test_answer_2():
    assert n_primos(2) == 1

def test_answer_4():
    assert n_primos(4) == 2

def test_answer_121():
    assert n_primos(121) == 30


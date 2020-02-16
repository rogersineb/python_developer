def primeiro_lex(lista):
    return min(lista)


def test_primeiro_lex():
    assert  primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A'

def test_primeiro_lex_2():
    assert primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA'


def conta_letras(frase, contar = "vogais"):
    contador = 0
    if contar == 'vogais':
        for i in range(len(frase)):
            if frase[i].lower() in ['a','e','i','o','u']:
                contador += 1
    elif contar == "consoantes":
        for i in range(len(frase)):
            if frase[i].lower() in ['b','c','d','f','g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
                contador += 1

    return contador

def test_conta_letras():
    assert conta_letras('programamos em python') == 6
    
def test_conta_letras_2():
    assert  conta_letras('programamos em python', 'vogais') == 6

def test_conta_letras_3():
    assert conta_letras('programamos em python', 'consoantes') == 13

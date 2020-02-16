def menor_string(strings):
    menor_palavra = strings[0].lower()

    for string in strings:
        if string.lower() < menor_palavra:
            menor_palavra = string.lower()
    return menor_palavra

def test_menor_string():
    assert menor_string(["ana", "maria", "José", "Valdemar"])  == "ana"
    

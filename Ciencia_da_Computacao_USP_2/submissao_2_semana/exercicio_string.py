def menor_nome(lista_nomes):
    menor = lista_nomes[0].strip().capitalize()
    for nome in lista_nomes:
        if len(menor) > len(nome.strip()):
            menor = nome.strip().capitalize()
    return menor


def test_mn():
    assert menor_nome(["   ana    ", "    josé", "Arquibaldo    ", "   Alouhis"]) == "Ana"

def test_mn_1():
    assert menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José'

def test_mn_2():
    assert menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José'

def test_mn_3():
    assert menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José'

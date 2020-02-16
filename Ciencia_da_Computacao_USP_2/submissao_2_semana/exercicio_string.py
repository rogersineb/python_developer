def modifica_nome(lista_nomes):
    menor_nome = lista_nomes[0].strip().capitalize()
    for nome in lista_nomes:
        if len(menor_nome) > len(nome.strip()):
            menor_nome = nome.strip().capitalize()
    return menor_nome


def test_mn():
    lista_nomes = ["   ana    ", "    josé", "Arquibaldo    ", "   Alouhis"]
    assert modifica_nome(lista_nomes) == "Ana"

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    grau_similaridade = 0
    i = 1

    while i < 7:
        grau_similaridade += (abs(as_a[i-1] - as_b[i-1])) / 6
        i+=1

    return round(grau_similaridade,2)
    
def calcula_assinatura(texto):
    tamanho_medio_palavra = calcula_tmp(texto)
    type_token = calcula_tt(texto)
    hapax_legomana = calcula_hl(texto)
    tamanho_medio_setenca = calcula_tms(texto)
    complexo_setenca = calcula_cs(texto)
    tamanho_media_frase = calcula_tmf(texto)

    return [tamanho_medio_palavra,
                                 type_token,
                             hapax_legomana,
                      tamanho_medio_setenca,
                           complexo_setenca,
                        tamanho_media_frase
    ]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n)
        do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas_textos = []
    for texto in textos:
        assinaturas_textos.append(calcula_assinatura(texto))

    probabilidades_textos = []
    for i in range(len(assinaturas_textos)):
        probabilidade = compara_assinatura(assinaturas_textos[i], ass_cp)
        probabilidades_textos.append([probabilidade, i+1])

    return min(probabilidades_textos)[1]    



def lista_frases(sentencas):
    conjunto_frases = []
    for sentenca in sentencas:
        frases_sentenca = separa_frases(sentenca)
        for frase in frases_sentenca:
            conjunto_frases.append(frase)

    return conjunto_frases

def lista_palavras(frases):
    conjunto_palavras = []
    for frase in frases:
        palavras_frase = separa_palavras(frase)
        for palavra in palavras_frase:
            conjunto_palavras.append(palavra)

    return conjunto_palavras

def calcula_tmp(texto):
    soma_tamanho_palavra = 0

    palavras = lista_palavras(lista_frases(separa_sentencas(texto)))
    for palavra in palavras:
        soma_tamanho_palavra += len(palavra)

    return soma_tamanho_palavra/len(palavras)

def calcula_tt(texto):
    palavras = lista_palavras(lista_frases(separa_sentencas(texto)))

    return n_palavras_diferentes(palavras) / len(palavras)

def calcula_hl(texto):
    palavras = lista_palavras(lista_frases(separa_sentencas(texto)))

    return n_palavras_unicas(palavras) / len(palavras) 
    

def calcula_tms(texto):
    sentencas = separa_sentencas(texto)

    soma_sentenca = 0
    for sentenca in sentencas:
        soma_sentenca += len(sentenca)

    return soma_sentenca / len(sentencas)
        
def calcula_cs(texto):
    sentencas = separa_sentencas(texto)
    frases = lista_frases(sentencas)

    return len(frases) / len(sentencas)

def calcula_tmf(texto):
    frases = lista_frases(separa_sentencas(texto))
    soma_caracteres_frases = 0
    for frase in frases:
        soma_caracteres_frases += len(frase)

    return soma_caracteres_frases / len(frases)

def test_calculo():
    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    assert calcula_assinatura(texto) == [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]


def test_compara_ass():
    assert compara_assinatura([4.34, 0.05, 0.02, 12.81, 2.16, 0.0],[3.96, 0.05, 0.02, 22.22, 3.41, 0.0]) == 1.84

def test_avalia_texto():
    ass_cp =[4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    textos = ["Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.",
              "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.",
              "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."]
    
    assert avalia_textos(textos, ass_cp) == 2























        

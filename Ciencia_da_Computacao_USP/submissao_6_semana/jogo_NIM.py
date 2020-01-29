def computador_escolhe_jogada(n, m):
    i = 1
    proxima_jogada = m
    while i <= m:
        if (n - i) % (m+1) == 0:
            proxima_jogada = i
        i += 1
    if proxima_jogada != m:
        print("O computador tirou", proxima_jogada, "peças")
        return proxima_jogada
    else:
        print("O computador tirou", m, "peças")
        return m

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada < 1 or jogada > n:
        jogada = int(input("Oops! Jogada inválida! Tente de novo: "))
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    qnt_pecas_restantes = n
    
    if n % (m+1) == 0:
        print("Você começa")
        
        while qnt_pecas_restantes > 0:
            qnt_pecas_restantes -= usuario_escolhe_jogada(qnt_pecas_restantes, m)
            print("Agora restam", qnt_pecas_restantes, "no tabuleiro")
            if qnt_pecas_restantes <= 0:
                print("Você ganhou!")
            else:
                qnt_pecas_restantes -= computador_escolhe_jogada(qnt_pecas_restantes, m)
                print("Agora restam", qnt_pecas_restantes, "no tabuleiro")

                if qnt_pecas_restantes <= 0:
                    print("O computador ganhou!")
    else:
        while qnt_pecas_restantes > 0:
            qnt_pecas_restantes -= computador_escolhe_jogada(n, m)
            print("Agora restam", qnt_pecas_restantes, "no tabuleiro")
            if qnt_pecas_restantes <= 0:
                print("O computador ganhou!")
            else:
                qnt_pecas_restantes -= usuario_escolhe_jogada(n, m)
                print("Agora restam", qnt_pecas_restantes, "no tabuleiro")

                if qnt_pecas_restantes <= 0:
                    print("Você ganhou!")

partida()
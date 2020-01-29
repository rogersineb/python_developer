def computador_escolhe_jogada(n, m):
    i = 1
    proxima_jogada = m
    while i <= m:
        if (n - i) % (m+1) == 0:
            proxima_jogada = i
        i += 1
    print("Foram removidas", proxima_jogada, "peças na última jogada")
    print()
    return proxima_jogada
    
def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    print()
    while jogada > m or jogada < 1 or jogada > n:
        print()
        jogada = int(input("Oops! Jogada inválida! Tente de novo: "))
    print("Foram removidas", jogada, "peças na última jogada")
    print()
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    qnt_pecas_restantes = n
    
    if n % (m+1) == 0:
        print()
        print("Você começa")
        print()
        while qnt_pecas_restantes > 0:
            qnt_pecas_restantes -= usuario_escolhe_jogada(qnt_pecas_restantes, m)
            print("Agora restam", qnt_pecas_restantes, "no tabuleiro")
            print()
            if qnt_pecas_restantes <= 0:
                print("Você ganhou!")
                print()
                return "v"
            else:
                qnt_pecas_restantes -= computador_escolhe_jogada(qnt_pecas_restantes, m)
                print("Agora restam", qnt_pecas_restantes, "no tabuleiro")
                print()
                if qnt_pecas_restantes <= 0:
                    print("O computador ganhou!")
                    print()
                    return "p"
    else:
        while qnt_pecas_restantes > 0:
            qnt_pecas_restantes -= computador_escolhe_jogada(qnt_pecas_restantes, m)
            print("Agora restam", qnt_pecas_restantes, "no tabuleiro")
            print()
            if qnt_pecas_restantes <= 0:
                print("O computador ganhou!")
                print()
                return "p"
            else:
                qnt_pecas_restantes -= usuario_escolhe_jogada(qnt_pecas_restantes, m)
                print("Agora restam", qnt_pecas_restantes, "no tabuleiro")
                print()
                if qnt_pecas_restantes <= 0:
                    print("Você ganhou!")
                    print()
                    return "v"

def campeonato():
    i = 0
    vitorias_usuario = 0
    vitorias_computador = 0
    while i < 3:
        print("**** Rodada", i+1, "****")
        print()
        vencedor = partida()
        if vencedor == "p":
            vitorias_computador += 1
        else:
            vitorias_usuario += 1
        i += 1
    print()    
    print("**** Final do campeonato! ****")
    print()    
    print("Placar: Você", vitorias_usuario, "X", vitorias_computador, "Computador")

def main():
    print("Bem-vindo ao jogo do Nim! Escolha: ")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print()
    tipo_jogo = int(input())
    
    if tipo_jogo == 1:
        print("Você escolheu uma partida isoalda!")
        partida()

    if tipo_jogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
main()
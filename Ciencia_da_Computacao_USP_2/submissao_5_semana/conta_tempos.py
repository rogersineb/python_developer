import time
import random
import ordenador



class ContaTempos:
    def lista_aleatoria(self, numero):
        lista = [random.randrange(1000) for x in range(numero)]
        return lista

    def lista_quase_ordenada(self, numero):
        lista = [x for x in range(numero)]
        lista[numero//10] = -500
        return lista

    def compara (self, numero):
        lista1 = self.lista_aleatoria(numero)
        lista2 = lista1[:]

        o = Ordenador()

        print("Comparando com listas aleatórias")    
        antes = antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou", depois - antes, "Segundos")        

        antes = antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes, "Segundos")


        lista1 = self.lista_quase_ordenada(numero)
        lista2 = lista1[:]

        print("\nComparando com listas quase ordenadas")    
        antes = antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("Bolha curta demorou", depois - antes, "Segundos")        

        antes = antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecao direta demorou ", depois - antes, "Segundos")

import ordenador
import conta_tempos
import pytest

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def c(self):
        return conta_tempos.ContaTempos()
    
    @pytest.fixture
    def l_quase(self, c):
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self, c):
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_bolha_curta_aleat(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta_aleat(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_l_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_l_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)

                               
                               
                               

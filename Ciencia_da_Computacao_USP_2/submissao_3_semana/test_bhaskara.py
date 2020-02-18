import refatoracao
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return refatoracao.Bhaskara()

    @pytest.mark.parametrize("entrada_a, entrada_b, entrada_c, esperado", [
        (1,0,0, (1,0)),
        (1, -5, 6,(2, 3, 2)),
        (10, 10, 10,0),
        (10, 20, 10,(1, -1))
        ])
    
    def testa_raiz(self, b, entrada_a, entrada_b, entrada_c, esperado):
        assert b.calcula_raizes(entrada_a, entrada_b, entrada_c) == (esperado)

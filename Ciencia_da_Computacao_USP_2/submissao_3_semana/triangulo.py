class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif self.a != self.b and self.a != self.c and self.c != self.b:
            return "escaleno"
        elif (self.a == self.b and self.b != self.c) or (self.c == self.b and self.b != self.a) or (self.c == self.a and self.a != self.b):
            return "isósceles"

    def retangulo(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        if self.a / triangulo.a == self.b / triangulo.b and self.c / triangulo.c:
            return True
        else:
            return False

import pytest


@pytest.mark.parametrize("lado_a, lado_b, lado_c, esperado", [
    (1, 1, 1, 3),
    (2, 4, 6, 12),
    (4, 5, 10, 19)
    ])
def testa_triangulo(lado_a, lado_b, lado_c, esperado):
    assert Triangulo(lado_a, lado_b, lado_c).perimetro() == esperado    

@pytest.mark.parametrize("lado_a, lado_b, lado_c, esperado", [
    (1, 1, 1, "equilátero"),
    (2, 4, 6, "escaleno"),
    (4, 5, 4, "isósceles"),
    (5, 5, 4, "isósceles"),
    (3, 4, 4, "isósceles")
    ])
    
def testa_triangulo_(lado_a, lado_b, lado_c, esperado):
    assert Triangulo(lado_a, lado_b, lado_c).tipo_lado() == esperado


@pytest.mark.parametrize("lado_a, lado_b, lado_c, esperado", [
    (3, 4, 5, True),
    (1, 3, 5, False)
    ])
    
def testa_triangulo_retangulo(lado_a, lado_b, lado_c, esperado):
    assert Triangulo(lado_a, lado_b, lado_c).retangulo() == esperado

def test_semelhanca():
    assert Triangulo(2,2,2).semelhantes(Triangulo(4,4,4)) == True

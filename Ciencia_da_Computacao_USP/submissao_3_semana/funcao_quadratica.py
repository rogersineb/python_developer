import math

def delta(a, b, c):
    return b**2 - 4*a*c

def bhaskaraSoma(a, b, delta):
    return (-b + math.sqrt(delta)) / (2*a)

def bhaskaraSubtracao(a, b, delta):
    return (-b - math.sqrt(delta)) / (2*a)

def raizesReais(a, b, delta):
    return bhaskaraSoma(a, b, delta), bhaskaraSubtracao(a, b, delta)

def imprime_raizes(a, b, c):
    
    d = delta(a, b, c)
    
    if(d == 0):
        x1 = bhaskaraSoma(a, b, d)
        print("a raiz desta equação é", x1)
    else:
        if d < 0:
            print("esta equação não possui raízes reais")
        else:
            x1, x2 = raizesReais(a, b, d)
            if x1 <= x2 :
                print("as raízes da equação são", x1, "e", x2)
            else:
                print("as raízes da equação são", x2, "e", x1)

def main():

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a,b,c)

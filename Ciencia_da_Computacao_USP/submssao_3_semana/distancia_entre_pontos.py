import math

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

d =  math.sqrt((x - x2)**2 + (y - y2)**2)
print(d)

if d >= 10 :
    print("longe")
else:
    print("perto")



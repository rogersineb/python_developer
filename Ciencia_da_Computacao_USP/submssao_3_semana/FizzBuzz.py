numero = int(input("Digite o número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
else:    
    if numero % 3 == 0:
        print("Fizz")
    else:
        if numero % 5 == 0:
            print("Buzz")
        else: 
            print(numero)
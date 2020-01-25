def maximo(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num3:
        return num2
    if num3 > num1 and num3 > num2:
        return num3
    else:
        return num1
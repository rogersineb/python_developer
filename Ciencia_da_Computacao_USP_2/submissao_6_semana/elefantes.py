def incomodam(numero):
    if numero < 1 or type(numero) is not int:
        return ''
    else:
        if numero > 1:
            return "incomodam " + incomodam(numero - 1)
        else:
            return "incomodam " * numero


def elefantes(numero):
    if numero < 2:
        return ''
    else:
        if numero > 2: 
            return elefantes(numero-1) + str(numero-1) + " elefantes incomodam muita gente\n" + str(numero) + " elefantes " + incomodam(numero) + "muito mais\n"
        else:
            return "Um elefante incomoda muita gente\n" + str(numero) + " elefantes " + incomodam(numero) + "muito mais\n"
        

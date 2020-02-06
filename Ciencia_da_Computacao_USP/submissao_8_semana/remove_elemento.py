def remove_repetidos(lista):
    lista2 =[]
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    lista2.sort()
    return lista2

def test_rmv_item():
    assert remove_repetidos([2,4,2,2,3,3,1]) == [1,2,3,4]
            
        

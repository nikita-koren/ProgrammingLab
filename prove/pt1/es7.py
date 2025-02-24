#Scrivere una funzione che prende in input due liste e ritorna `True` se le due liste hanno almeno un elemento in comune

def comune (lista1, lista2):
    i = 0
    while i < 5:
        if (lista1[i] in lista2):
            return True
        i += 1
    else: 
        return False
    
lista1 = [1, 3, 7, 9, 0]
lista2 = [2, 7, 4, 6, 8]
print(comune(lista1, lista2))
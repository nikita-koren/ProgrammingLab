#Scrivete una funzione sum_list(my_list) (una manuale e una con sum)
#che sommi tutti gli elementi di una lista
#se la lista è vuota deve tornare None

def sum_manuale (lista):
    if not lista:
        return None
    somma = 0
    for elemento in lista:
        somma += elemento
    return somma

def sum_conf (lista):
    if lista:
        return sum(lista)
    else:
        return None


lista1 = [1, 5, 8, 9, 0]
lista2 = []

print('==============')
print(sum_manuale(lista1))
print('==============')
print(sum_conf(lista1))
print('==============')
print(sum_manuale(lista2))
print('==============')
print(sum_conf(lista2))
print('==============')

class InvalidParameter(Exception):
    pass

parametro = -5
if parametro < 0:
    raise InvalidParameter('Il parametro è minore di zero')

def somma_lista(lista_input):
    if not type(lista_input) == list:
        raise TypeError ('Il tipo di lista input non è lista ma {}'.format(type(lista_input)))
    somma = 0
    for elemento in lista_input:
        somma += elemento
    return somma
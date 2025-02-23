#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]

def cifre_inparole (lista):
    dizionario = {0 : 'zero', 1 : 'uno', 2 : 'due', 3 : 'tre', 4 : 'quattro', 
               5 : 'cinque', 6 : 'sei', 7 : 'sette', 8 : 'otto', 9 : 'nove'}
    parole = []
    for n in lista:
        parole.append (dizionario[n])
    return parole

numeri = [1, 0, 7, 9, 8, 4, 3, 6, 2, 5]
print(cifre_inparole(numeri))
#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una lista di
#stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]

dizionario = {0 : 'zero', 1 : 'uno', 2 : 'due', 3 : 'tre', 4 : 'quattro', 5 : 'cinque', 6 : 'sei', 7 : 'sette', 8 : 'otto', 9 : 'nove'}

def n_inparola (A):
    B = []
    for i in range (len(A)):
        B.append(dizionario[A[i]])
    return B

A = [2, 5, 7, 9, 0, 3, 6]
print(A)
print('==========')
print(n_inparola(A))
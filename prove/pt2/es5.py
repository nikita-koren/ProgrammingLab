#Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di A[i] con A[j].

def scambia (A, i, j):
    tmp = A[j]
    A[j] = A[i]
    A[i] = tmp
    return A

A = (scambia([1, 2, 3, 4], 0, 2))
print(A)
#Definite la funzione fattoriale

def fattoriale (n):
    if (n < 0):
        return 0
    if (n == 0 | n == 1):
        return 1
    else:
        return n * fattoriale(n - 1)

prova = fattoriale(5)
print(prova)
#6. Definite la funzione fattoriale

def fattoriale (n):
    if (n < 0):
        return 0
    elif (n == 0 or n == 1):
        return 1
    else:
        return (n * fattoriale(n - 1))

print('==============')
print(fattoriale(12))
print('==============')
print(fattoriale(-1))
print('==============')
print(fattoriale(5))
print('==============')
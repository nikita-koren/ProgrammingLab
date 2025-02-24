#Scrivere una funzione che prende in input due liste e ritorna `True` se le due liste hanno almeno un
#elemento in comune

def comune (A, B):
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            if A[i] ==  B[j]:
                return True
    else:
        return False
            
A = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
B = [1, 3, 5, 7, 9]
C = [0, 2, 4, 6, 8]
D = [0]

print('==============')
print(comune(A, B)) #ja
print('==============')
print(comune(C, B)) #ne
print('==============')
print(comune(D, B)) #ne
print('==============')
print(comune(A, C)) #ja
print('==============')
print(comune(C, D)) #ja
print('==============')
print(comune(A, D)) #ne

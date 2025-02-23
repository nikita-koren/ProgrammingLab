#Definire una funzione che dati 3 numeri interi 
# stabilisce se possono essere i valori dei lati di un 
# triangolo e se si di che tipo di triangolo

def triangolo (a, b, c):
    if (a < (b + c) and b < (a + c) and c < (a + b)):
        if(a == b == c): 
            print("il triangolo è EQUILATERO")
        elif((a != b and a == c & b != c) or (a == b & a != c & b != c) or (a != b & a != c & b == c)): 
            print("il triangolo è ISOSCELE")
        else: 
            print("il triangolo è SCALENO")
        return True
    
    else:
        return False

print("=====")
print(triangolo(3, 4, 5))
print("=====")
print(triangolo(4, 4, 4))
print("=====")
print(triangolo(2, 4, 2))
print("=====")

#Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un
#triangolo e se si di che tipo di triangolo
def Triangolo (a, b, c):
    if ((a + b) > c and (b + c) > a and (a + c) > b):
        if(a == b == c): 
            print("il triangolo è EQUILATERO")
        elif((a != b and a == c & b != c) or (a == b & a != c & b != c) or (a != b & a != c & b == c)): 
            print("il triangolo è ISOSCELE")
        else: 
            print("il triangolo è SCALENO")
        return True
    else:
        return False
    
def intrepreta_triangolo (a, b, c):        
    if Triangolo (a,b,c) == True:
        print("è un TRIANGOLO")
    else:
        print("NON è un TRIANGOLO")


print("=====")
intrepreta_triangolo(3, 4, 5)
print("=====")
intrepreta_triangolo(4, 4, 4)
print("=====")
intrepreta_triangolo(2, 4, 2)
print("=====")
intrepreta_triangolo(1, 7, 2)
print("=====")
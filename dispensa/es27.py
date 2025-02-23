#Esempio di utilizzo del costrutto try-except.

mia_var = input()
try: 
    mia_var = float(mia_var)
except:
    print('Non posso convertire "mia_var" a numero!')
    print('Uso il valore di default di "0.0"')
mia_var = 0.0
print(mia_var) # Stampa a schermo 0.0
mia_stringa = 'Date,Sales\n'
lista_elementi = mia_stringa.split(',')
print(lista_elementi)

mia_stringa = '5.5'
mio_numero = float(mia_stringa)
print(mia_stringa)

mia_lista = [1,2,3]
mia_lista.append(4)
print(mia_lista)

#prova lista
values = []
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    elements = line.split(',')
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]
        values.append(value)
print(values)

def sum_csv(file_name):
    with open('shampoo_sales.cvs', 'r') as file:
        lines = file.readlines()
        total_sales = 0.0
        
    for line in lines[1:]:  # Salta la prima riga (intestazione)
         # Dividi la riga in colonne
        elements = line.strip().split(',')
                
        # Controlla che ci siano almeno 2 elementi (data e valore)
        if len(elements) == 2:
            # Converti il valore delle vendite in float e aggiungilo alla somma
             total_sales += float(elements[1])
            except ValueError:
        print(f"Valore non valido nella riga: {line}")
            continue
    return total_sales

    except FileNotFoundError:
     print(f"Errore: Il file '{file_name}' non esiste.")
        return None

# Esempio di utilizzo
file_name = 'shampoo_sales.csv'
somma = sum_csv(file_name)
if somma is not None:
    print(f"La somma delle vendite è: {somma}")
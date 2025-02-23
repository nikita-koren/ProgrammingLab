#Nel seguente esempio, si legge da shampoo_sales.csv e si
#popola la lista dati che ne conterrà le informazioni:

dati = []
with open('shampoo_sales.csv', 'r') as my_file:
    for line in my_file:
        elemento = line.split(',')
        if (elemento [0] != 'Date'):
            data = elemento[0]
            valore = float(elemento[1])
            dati.append([data, valore])
print(dati)
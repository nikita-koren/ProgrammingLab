#Nel seguente esempio, si legge da shampoo_sales.csv e si
#popola la lista dati che ne conterrà le informazioni:

# Inizializzo una lista vuota per salvare i dati
dati = []
# Apro e leggo il file, linea per linea
with open('shampoo_sales.csv', 'r' ) as mio_file:
    for linea in mio_file:
        # Faccio lo split di ogni riga sulla virgola
        elementi = linea.split(',')
        # Se NON sto processando l’intestazione...
        if elementi[0] != 'Date':
            # Setto le variabili data e il valore,
            # convertendo il valore a floating point
            data = elementi[0]
            valore = float(elementi[1])
            # Aggiungo alla lista dei dati
            dati.append([data,valore])
print(dati)
prova = dir(dati)
print(prova)
nznam = type(dati)
print(nznam)
vidmo = type(nznam)
print(vidmo)
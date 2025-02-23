#il seguente snippet di codice apre il file in modalità lettura, ne stampa
#i primi 80 caratteri usando lo slicing delle stringe e lo chiude

mio_file = open('shampoo_sales.csv', 'r')
print(mio_file.read()[0:80])
mio_file.close()

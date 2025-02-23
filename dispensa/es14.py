#Il seguente snippet invece, apre il file in modalità lettura,
#legge e stampa le prime 5 righe e lo chiude

my_file  = open('shampoo_sales.csv', 'r')
for i in range(5):
    print(my_file.readline())
my_file.close()

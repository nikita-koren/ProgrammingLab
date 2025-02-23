#Un file letto all’interno di un contesto di esecuzione, riga
#per riga in modo pythonico

with open('shampoo_sales.csv', 'r') as my_file:
    for line in my_file:
        print(line)
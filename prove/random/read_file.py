# Apri il file in modalità lettura
try:
    with open('shampoo_sales.csv', 'r') as my_file:
        # Leggi il contenuto del file
        content = my_file.read()
        print(content)
except FileNotFoundError:
    print("Errore: Il file 'shampoo_sales.csv' non esiste nella directory corrente.")
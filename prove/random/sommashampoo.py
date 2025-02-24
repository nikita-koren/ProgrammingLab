def sum_csv(file_name):
        # Apri il file in modalità lettura
        with open(file_name, 'r') as file:
            # Leggi tutte le righe del file
            lines = file.readlines()
            
            # Inizializza la somma
            total_sales = 0.0

            # Salta l'intestazione e processa le righe
            for line in lines[1:]:  # Escludi la prima riga (intestazione)
                elements = line.strip().split(',')
                
                # Controlla che ci siano almeno 2 elementi
                if len(elements) == 2:
                    try:
                        # Somma il valore delle vendite
                        total_sales += float(elements[1])
                    except ValueError:
                        print(f"Valore non valido nella riga: {line}")
            
            return total_sales
file_name = 'shampoo_sales.csv'
somma = sum_csv(file_name)
print ('la somma è: {}' .format(somma))
  
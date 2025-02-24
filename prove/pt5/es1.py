def sum_csv(file_name):
    try:
        with open(file_name,'r') as file:
            valori = []
            for riga in file:
                valore = riga.split(',')
                if valore[0] != 'Date':                    
                    data = valore[0]
                    try:
                        numero = float(valore[1])                
                        valori.append(numero)
                    except ValueError:
                        continue
            return sum(valori)
    except IOError:
        print('Non posso leggere il file!')
    except FileNotFoundError:
        print('Non riesco a trovare il file!')
    except Exception as error:
        print('Errore generico: {}'.format(error))

prova = 'shampoo_sales.csv'
print(sum_csv(prova))
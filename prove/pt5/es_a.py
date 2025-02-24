class CSV_File ():
    
    def __init__ (self, nome_file):
        self.nome = nome_file
        self.data = []
    
    def get_data(self):
        try:
            with open (self.nome, 'r') as file:
                righe = file.readlines()
                for riga in righe:
                    self.data.append(riga.split(','))
                return self.data
        except FileNotFoundError as error:
            return error
        except IOError: 
            print('Non posso leggere il file!')
        except FileNotFoundError:
            print('Non riesco a trovare il file!')
        
csv_file = CSV_File('shampoo_sales.csv')
dati = csv_file.get_data()

if dati is not None:
    print(dati)

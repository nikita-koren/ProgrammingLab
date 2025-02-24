#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo“get_data()” che torni i dati dal file CSV come lista di liste


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
        
csv_file = CSV_File('shampoo_sales.csv')
dati = csv_file.get_data()

if dati is not None:
    print(dati)

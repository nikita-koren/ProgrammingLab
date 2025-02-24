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
        except IOError: 
            print('Non posso leggere il file!')
        except FileNotFoundError:
            print('Non riesco a trovare il file!')

class NumericalCSVFile (CSV_File):
    def get_data(self):
        dati_originali = super().get_data()
        if dati_originali == None:
            return None
        
        dati_numerici = []
        for valori in dati_originali[1::]:
                try:
                    data = valori[0]
                    numero = float(valori[1])
                    dati_numerici.append(numero)
                except TypeError:
                    print("ERRORE")
                    continue
                except ValueError:
                    print("ERRORE")
                except IndexError:
                    print("ERRORE")

        return dati_numerici

csv_file = CSV_File('shampoo_sales.csv')
print(csv_file.get_data())

num_csv_file = NumericalCSVFile('shampoo_sales.csv')
print(num_csv_file.get_data())
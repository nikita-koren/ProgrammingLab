class CSVFile ():

    def __init__ (self, name):
        if not  isinstance(name, str):
            raise TypeError('Era richiesta una stringa non: {}'.format(type(name)))

        self.name = name
        self.dati = []
    
    def get_data (self, start = None, end = None):
        try:
            with open(self.name, 'r') as file:
                righe = file.readlines()

                if not righe:
                    return self.dati

                dati = [riga.strip().split(',') for riga in righe]

                if len(dati) == 1:
                    return self.dati
                
                dati = dati[1::]
                
                if start is not None:
                    if(start < 1 and not isinstance(start, int)) and start > len(dati):
                        raise ValueError ('ERRORE! Start deve essere un numero intero maggiore di 1 e non {}'.format(start))
                if end is not None:
                    if(end < 1 and not isinstance(start, int)) and end > start:
                        raise ValueError ('ERRORE! Start deve essere un numero intero maggiore di 1 e non {}'.format(end))
                
                start = (start - 1) if start else 0
                end = end if end else len(dati)

                valori = dati[start:end]
                for valore in valori:
                    self.dati.append(valore)

                return self.dati
        except IOError:
            print('Non posso leggere il file!')
            return None
        except FileNotFoundError:
            print('Non riesco a trovare il file!')
            return None

class NumericalCSVFile (CSVFile):
    def get_data (self, *args, **kwargs):
        csv_data = super().get_data(*args, **kwargs)
        if csv_data == None:
            return None
        
        dati_numerici = []
        for valori in csv_data:
            try:
                data = valori[0]
                numero = float(valori[1])
                dati_numerici.append(numero)
            except TypeError:
                print("ERRORE")
                continue
            except ValueError:
                print("ERRORE")
                continue
            except IndexError:
                print("ERRORE")
        return dati_numerici
    
nome = 'shampoo_sales.csv'
funzione = CSVFile(nome)
print(funzione.get_data())

print(funzione.get_data(start=1, end=16))

print(funzione.get_data(start=3))


nome2 = 'shampoo_sales.csv'
funzione2 = NumericalCSVFile(nome)

print(funzione2.get_data(start=1, end=16))

print(funzione2.get_data(start=3))

print(sum(funzione2.get_data()))
class CSVFile ():
    def __init__ (self, name):
        if not isinstance (name, str):
            raise TypeError ('Era richiesta una stringa non: {}'.format(type(name)))

        self.name = name
        self.lista = []
    
    def get_data(self, start = None, end = None): #vuol dire che sono opzionali
        try:
            with open(self.name, 'r') as file:
                righe = file.readlines()

                if not righe:
                    return self.lista
                
                valori = [riga.strip().split(',') for riga in righe]
                if len(valori) == 1:
                    return self.lista
                
                valori = valori[1::] #escludiamo la prima riga

                if start is not None:
                    if not isinstance(start, int) or start < 1 or start > len(valori):
                        raise TypeError ('ERRORE! Start deve essere un numero intero maggiore di 1 e non {}'.format(start))
                if end is not None:
                    if not isinstance(end, int) or end < (start if start else 1) or end > len(valori):
                        raise TypeError ('ERRORE! End deve essere un numero intero maggiore di start, non {}'.format(start))
                
                
                start = (start - 1) if start else 0
                end = end if end else len(valori)
                
                dati = valori[start : end]
                for dato in dati:
                    self.lista.append(dato)
                return self.lista
            
        except FileNotFoundError:
            print('Non riesco a trovare il file!')
            return None
        except IOError:
            print('Non posso leggere il file!')
            return None
        
nome = 'shampoo_sales.csv'
funzione = CSVFile(nome)
print(funzione.get_data())

print(funzione.get_data(start=1, end=16))

print(funzione.get_data(start=3))
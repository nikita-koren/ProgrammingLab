class CSVfile():
    def __init__(self, name):
        try:
            open(name)
        except: 
            print('errore: il file inserito non esiste')
        self.name = name
    
    def get_data(self):
        file = open(self.name)
        file = file.read()
        l1 = file.split('\n')
        lista = []
        for item in l1:
            if item == '':
                l2 = item.split(',')
                if l2(0) != 'Date' :
                    lista.append(l2)
        file.close()
        return lista
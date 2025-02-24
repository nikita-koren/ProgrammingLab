class CSVFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Il nome del file deve essere una stringa")
        self.name = name

    def get_data(self, start=None, end=None):
        try:
            with open(self.name, 'r') as file:
                righe = file.readlines()

                # Se il file è vuoto, restituisci una lista vuota
                if not righe:
                    return []

                # Rimuoviamo spazi e newline e dividiamo le righe
                dati = [riga.strip().split(',') for riga in righe]

                # Se il file ha solo l'intestazione, restituisci []
                if len(dati) == 1:
                    return []

                # Escludi la prima riga (intestazione)
                dati = dati[1:]

                # Controlla che start e end siano numeri validi
                if start is not None:
                    if not isinstance(start, int) or start < 1:
                        raise ValueError("start deve essere un intero positivo")

                if end is not None:
                    if not isinstance(end, int) or end < start:
                        raise ValueError("end deve essere un intero maggiore o uguale a start")

                # Correggi il slicing per includere 'end'
                return dati[start - 1:end] if start is not None else dati
        
        except FileNotFoundError:
            print('Non riesco a trovare il file!')
            return []
        except IOError:
            print('Non posso leggere il file!')
            return []
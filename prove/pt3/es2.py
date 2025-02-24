#Definire una funzione che prende in input un file e costruisce un 
#dizionario con chiavi la lettere iniziali e con valore le parole di 
#lunghezza maggiore contenute nel file che iniziano con quelle lettere.

def dizionario_parole_piulunghe (my_file):
    dizionario = {}
    try:
        with open(my_file, 'r') as file:
            testo = file.read().lower()

            # Rimuove manualmente la punteggiatura
            punteggiatura = ".,!?;:-_()[]{}\"'’'«»"
            for segno in punteggiatura:
                testo = testo.replace(segno, ' ')
            
            parole = testo.split()

            for parola in parole:
                prima_lettera = parola[0]
                if prima_lettera not in dizionario:
                    dizionario[prima_lettera] = parola
                else:
                    if len(parola) > len(dizionario[prima_lettera]):
                        dizionario[prima_lettera] = parola
            for lettera in sorted(dizionario):
                print('lettera[{}] == {}'.format(lettera, dizionario[lettera]))
            return dizionario
    
    except FileNotFoundError as error:
        print(error)
        return None

# Test della funzione
nome_file = "testo.txt"  # Assicurati che il file esista
risultato = dizionario_parole_piulunghe(nome_file)

            

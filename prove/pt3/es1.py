#Definire una funzione che prende in input un file ed una parola e conta quante volte
#quella parola è presente sul file

def conta_parola (nome_file, parola):
    count = 0
    try:
        with open(nome_file, 'r') as file:            
            testo = file.read().lower()

            # Rimuove la punteggiatura manualmente
            punteggiatura = ".,!?;:-_()[]{}\"'«»"
            for segno in punteggiatura:
                testo = testo.replace(segno, " ")  # Sostituisce ogni segno con uno spazio
                
            parole = testo.split()
        for p in parole:
            if p == parola.lower():
                count += 1
        return count
    except FileNotFoundError as error:
        print(error)
        return None

nome_file = "testo.txt"  # Sostituisci con il nome del tuo file
parola_cercata = "giornata"

occorrenze = conta_parola(nome_file, parola_cercata)
if occorrenze is not None:
    print(f"La parola '{parola_cercata}' compare {occorrenze} volte nel file.")
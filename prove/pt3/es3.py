#Definire una funzione conteggio che prende come input un file e ritorna un dizionario
#con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia
#con quella parola. Considerare come inizio di frase qualsiasi parola che segue un
#punto, un punto esclamativo, un punto interrogativo o si trova all'inizio del testo.

def dizionario_inizio_frase (my_file):
    dizionario= {}
    try:
        with open(my_file, 'r') as file:
            testo = file.read().lower()

            for segno in ".!?":
                testo = testo.replace(segno, '.')
            
            frasi = testo.split('.')
            
            for frase in frasi:
                parole = frase.split()
                if parole:
                    prima_parola = parole[0]
                    if prima_parola not in dizionario:
                        dizionario[prima_parola] = 1
                    else:
                        dizionario[prima_parola] += 1
            
            return dizionario
    except FileNotFoundError as error:
        return error
    

# Test della funzione
nome_file = "testo.txt"  # Assicurati che il file esista
risultato = dizionario_inizio_frase(nome_file)
print(risultato)
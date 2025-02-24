#Definire una funzione legge prende come input un file, rimuove tutte 
# le righe duplicate, scrive il risultato in un nuovo file chiamato unique.txt.

def legge(my_file):
    try:
        with open(my_file, 'r') as file:
            righe = file.readlines()

            righe_uniche = []
            for riga in righe:
                if riga not in righe_uniche:
                    righe_uniche.append(riga)
        
        with open('unique.txt', 'w') as unique:
            for elemento in righe_uniche:
                unique.writelines(elemento)
    except FileNotFoundError as error:
        print(f"Errore: Il file '{my_file}' non è stato trovato.")                
file_importato = 'testo.txt'
print(legge(file_importato))
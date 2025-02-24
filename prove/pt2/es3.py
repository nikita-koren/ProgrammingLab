class Palindromo:
    def __init__(self, parola):
        self.parola = parola  # Memorizza la parola

    def controlla_palindromo(self):
        return self.parola == self.parola[::-1]  # Confronta la parola con la sua versione invertita

# Esempio di utilizzo
prova1 = Palindromo("anna")
print(prova1.controlla_palindromo())  

prova2 = Palindromo("ciao")
print(prova2.controlla_palindromo())  
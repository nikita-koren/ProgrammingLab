class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("Ciao, sono {} {}".format(self.nome, self.cognome)) 

persona1 = Persona('Mario', 'Rossi')
persona2 = Persona('Irene', 'Bianchi')
print(persona1.nome)
print(persona2.cognome)
persona1.saluta()
persona2.saluta()

persone = [Persona('Giorgio','Verdi'), Persona('Laura','Gialli')]
print(persone[0].nome)
persone[1].saluta()

class Studente(Persona):
    def saluta(self):
        print("Ciao, sono {} {} e sono uno studente".format(self.nome, self.cognome))

class Professore(Persona):
    def __str__(self):
        return 'Prof. "{} {}"'.format(self.nome, self.cognome)
    # Si sovrascrive il metodo "saluta"
    def saluta(self):
        print ('Ciao, sono il Prof. {} {}'.format(self.nome, self.cognome))
        # Si ri-accede al metodo "saluta" originale usando super()
    def saluta_informale(self):
        super().saluta()

persona3 = Studente('Nikita', 'Koren')
persona4 = Professore('Paolo', 'Vicig')
print(persona3.nome)
print(persona4.cognome)
persona3.saluta()
persona4.saluta()
persona4.saluta_informale()

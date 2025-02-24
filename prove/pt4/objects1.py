import random

class Persona():

    def __init__ (self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__ (self):
        return 'Persona: "{} {}"'.format(self.nome, self.cognome)
    
    def ciao(self):
        #genera un numero casuale tra 0, 1, 2
        numero_random = random.randint(0,2)

        if numero_random == 0:
            print('Ciao, sono {} {}'.format(self.nome, self.cognome))
        elif numero_random == 1:
            print('Salve, sono {}'.format(self.nome))
        elif numero_random == 2:
            print('Yo bro, sono {}'.format(self.nome))

person = Persona('Mario', 'Rossi')
person.ciao()
print(person.__str__())


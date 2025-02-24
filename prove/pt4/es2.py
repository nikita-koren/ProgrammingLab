
class Veicolo (): #modello, marca, anno, speed
    def __init__ (self, anno, modello, marca ):
        self. modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__ (self):
        return 'Dettagli della macchina: \n marca = {} \n modello = {} \n anno = {} \nvelocità = {} \n'.format(self.marca, self.modello, self.anno, self.speed)
    
    def accellerare (self):
        self.speed += 5
        print(f"Velocità aumentata: {self.speed} km/h")
        return self.speed
    
    def frenare (self):
        if (self.speed > 0):
            self.speed -= 5
            print(f"Velocità ridotta: {self.speed} km/h")
        return self.speed

    def get_speed(self):
     return 'velocità corrente = {} km/h'.format(self.speed)



veicolo = Veicolo(2022, "Fiat Panda", "Fiat")
print(veicolo)
veicolo.accellerare()
veicolo.accellerare()
veicolo.frenare()
print(veicolo.get_speed())
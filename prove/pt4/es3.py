
class Veicolo (): #modello, marca, anno, speed
    def __init__ (self, anno, modello, marca):
        self. modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__ (self):
        return 'Dettagli della macchina: \nmarca = {} \nmodello = {} \nanno = {} \nvelocità = {} \n'.format(self.marca, self.modello, self.anno, self.speed)
    
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

class Auto (Veicolo):
    def __init__(self, anno, modello, marca, numero_porte):
        super().__init__(anno, modello, marca)
        self.numero_porte = numero_porte

    def __str__ (self):
        return 'Dettagli della macchina: \nmarca = {} \nmodello = {} \nanno = {} \nvelocità = {} \nnumero porte = {}'.format(self.marca, self.modello, self.anno, self.speed, self.numero_porte)

class Moto (Veicolo):
    def __init__ (self, anno, modello, marca, tipo):
        self. modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
        self.tipo = tipo

    def __str__ (self):
        return 'Dettagli della moto: \nmarca = {} \nmodello = {} \nanno = {} \nvelocità = {} \ntipo = {}'.format(self.marca, self.modello, self.anno, self.speed, self.tipo)

veicolo = Veicolo(2022, "Fiat Panda", "Fiat")
print(veicolo)
veicolo.accellerare()
veicolo.accellerare()
veicolo.frenare()
print(veicolo.get_speed())
print('================')
auto = Auto(2022, "Fiat Panda", "Fiat", 4)
moto = Moto(2021, "Ducati Panigale", "Ducati", "Sportiva")

print(auto)
auto.accellerare()
auto.frenare()
print(auto.get_speed())
print('================')

print(moto)
moto.accellerare()
moto.frenare()
print(moto.get_speed())
print('================')

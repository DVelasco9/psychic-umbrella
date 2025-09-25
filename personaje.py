class personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza: ", self.fuerza)
        print("Vida: ", self.vida)
        print("Defensa: ", self.defensa)
        print("Inteligencia: ", self.inteligencia)

    def subir_nivel(self, fuerza, vida, defensa, inteligencia):
        self.fuerza = fuerza + fuerza
        self.vida = vida + vida
        self.defensa = defensa + defensa 
        self.inteligencia = inteligencia + inteligencia

mi_personaje = personaje("XFire", 15, 5, 150, 50)

mi_personaje.atributos()

mi_personaje.subir_nivel(5, 10, 5, 0)
mi_personaje.atributos()
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
        print("Inteligencia: ", self.inteligencia)
        print("Vida: ", self.vida)
        print("Defensa: ", self.defensa)

    def subir_nivel(self, fuerza, vida, defensa, inteligencia):
        self.fuerza = self.fuerza + fuerza
        self.vida = self.vida + vida
        self.defensa = self.defensa + defensa 
        self.inteligencia = self.inteligencia + inteligencia

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, "ha realizado", damage ,"puntos de daño a", enemigo.nombre) 
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


mi_personaje = personaje("XFire", 15, 5, 150, 50)
mi_personaje.atributos()
mi_personaje.subir_nivel(0, 0, 0, 0)

mi_enemigo = personaje("common", 10, 0, 15, 3)
mi_enemigo.atributos()

mi_personaje.atacar(mi_enemigo)

mi_enemigo.atributos()

dog = personaje("EL JAJAS", 1000, 1000, 1000, 1000)
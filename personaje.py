from abc import ABC, abstractmethod

class personaje(ABC):
    
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.__vida = vida
        self.defensa = defensa

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("°Fuerza: ", self.fuerza)
        print("°Inteligencia: ", self.inteligencia)
        print("°Vida: ", self.__vida)
        print("°Defensa: ", self.defensa)

    def subir_nivel(self, fuerza, vida, defensa, inteligencia):
        self.fuerza = self.fuerza + fuerza
        self.__vida = self.__vida + vida
        self.defensa = self.defensa + defensa 
        self.inteligencia = self.inteligencia + inteligencia

    @staticmethod
    def walk():
        print("El personaje camina")

    def esta_vivo(self):
        return self.__vida > 0
    
    
    def _morir(self):
        self.__vida = 0
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        return max(0, daño)
    
    
    def atacar(self, enemigo):
        daño = self.damage(enemigo)
        if daño == 0:
            print(f"{self.nombre} no logró hacer daño a {enemigo.nombre} (defensa demasiado alta).")
            return
        enemigo.__vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.__vida)
        else:
            enemigo._morir()

    @abstractmethod
    def sound(self):
       pass

class guerrero(personaje):
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, espada):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.espada = espada



    def cambiar_arma(self):
        opcion = int(input(f"Elige un arma: (1) Acero Valyrio, daño 8, (2) matadragones, daño 10: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("°Espada: ", self.espada)
        
    def damage(self, enemigo):
        daño = self.fuerza * self.espada - enemigo.defensa
        return max(0, daño)
    
    


    def sound(self):
        print("SLASH")

class mago(personaje):
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, libro):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("°libro", self.libro)

    def damage(self, enemigo):
        daño = self.inteligencia * self.libro - enemigo.defensa
        return max(0, daño)

    def sound(self):
        print("CARTERA")


class enemy_p(personaje):
    poison = 0

    @classmethod
    def hemorragia(cls):
        cls.poison = 5

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, truco, poison=None):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.truco = truco

        self.poison = poison if poison is not None else enemy_p.poison



    def atributos(self):
        super().atributos()
        print("°Truco", self.truco)
        print("°Veneno", self.poison)

   # def subir_nivel(self, fuerza, vida, defensa, inteligencia,):
    #    super().subir_nivel(fuerza, vida, defensa, inteligencia)

    def damage(self, enemigo):
        daño = self.truco * self.poison - enemigo.defensa
        return max(0, daño)

    def sound(self):
        print("sssss")

guts = guerrero("Guts", 20, 10, 100, 100, 5)
vanessa = mago("Vanessa", 5, 30, 50, 10, 5)


#guts.cambiar_arma()
#guts.espada
guts.atributos()
guts.subir_nivel(1,2,3,4)
guts.atributos()
#guts.walk()
#guts.sound()

enemy_p.hemorragia()
comun = enemy_p("common", 10, 0, 30, 5, 3)
comun.atributos()

comun.atacar(guts)

def combate(p1, p2):
    turno = 0
    while p1.esta_vivo() and p2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", p1.nombre, ":", sep="")
        p1.atacar(p2)
        print(">>> Acción de ", p2.nombre, ":", sep="")
        p2.atacar(p1)
        turno += 1
    if p1.esta_vivo():
        print(f"\n{p1.nombre} gana")
    elif p2.esta_vivo():
        print(f"\n{p2.nombre} gana")
    else: 
        print("\nEmpate")


combate(guts, vanessa)


#dog = personaje("EL JAJAS", 1000, 1000, 1000, 1000)

#guts.atacar()
#guts.atacar(dog)
#dog.atacar(guts)

#mi_personaje = personaje("XFire", 15, 5, 150, 50)
#mi_personaje.atributos()
#mi_personaje.subir_nivel(0, 0, 0, 0)

#mi_enemigo.atributos()

#mi_personaje.atacar(mi_enemigo)

#mi_enemigo.atributos()

#mi_personaje.set_fuerza(5)



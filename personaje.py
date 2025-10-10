# ============================================================
# PROGRAMA DE HERENCIA Y POLIMORFISMO CON CLASES ABSTRACTAS
# Autor: Diego
# ============================================================

from abc import ABC, abstractmethod

# ------------------------------------------------------------
# CLASE BASE ABSTRACTA: personaje
# ------------------------------------------------------------
class personaje(ABC):
    """
    Clase abstracta que define la estructura base de un personaje.
    Contiene atributos generales como fuerza, vida y defensa.
    """

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.__vida = vida           # Atributo privado
        self.defensa = defensa

    def atributos(self):
        """Muestra los atributos principales del personaje."""
        print(self.nombre, ":", sep="")
        print("°Fuerza:", self.fuerza)
        print("°Inteligencia:", self.inteligencia)
        print("°Vida:", self.__vida)
        print("°Defensa:", self.defensa)

    def subir_nivel(self, fuerza, vida, defensa, inteligencia):
        """Aumenta las estadísticas del personaje."""
        self.fuerza += fuerza
        self.__vida += vida
        self.defensa += defensa
        self.inteligencia += inteligencia

    @staticmethod
    def walk():
        """Método estático: todos los personajes pueden caminar."""
        print("El personaje camina")

    def esta_vivo(self):
        """Devuelve True si el personaje sigue con vida."""
        return self.__vida > 0

    def _morir(self):
        """Cambia la vida a 0 y muestra un mensaje de muerte."""
        self.__vida = 0
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        """
        Calcula el daño base infligido al enemigo.
        Daño = fuerza - defensa del enemigo.
        """
        daño = self.fuerza - enemigo.defensa
        return max(0, daño)

    def atacar(self, enemigo):
        """Ejecuta un ataque contra el enemigo y muestra el resultado."""
        daño = self.damage(enemigo)
        if daño == 0:
            print(f"{self.nombre} no logró hacer daño a {enemigo.nombre} (defensa demasiado alta).")
            return
        enemigo._personaje__vida -= daño  # Acceso al atributo privado
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo._personaje__vida)
        else:
            enemigo._morir()

    @abstractmethod
    def sound(self):
        """Método abstracto que cada subclase debe implementar."""
        pass


# ------------------------------------------------------------
# CLASE guerrero (hereda de personaje)
# ------------------------------------------------------------
class guerrero(personaje):
    """
    Clase que representa un guerrero con una espada.
    El daño depende de su fuerza y del arma equipada.
    """

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, espada):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.espada = espada

    def cambiar_arma(self):
        """Permite elegir una nueva espada con diferente daño."""
        opcion = int(input("Elige un arma: (1) Acero Valyrio (daño 8) | (2) Matadragones (daño 10): "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecto")

    def atributos(self):
        """Muestra los atributos, incluyendo el arma."""
        super().atributos()
        print("°Espada:", self.espada)

    def damage(self, enemigo):
        """Daño basado en fuerza multiplicada por el poder del arma."""
        daño = self.fuerza * self.espada - enemigo.defensa
        return max(0, daño)

    def sound(self):
        """Sonido característico del guerrero."""
        print("SLASH")


# ------------------------------------------------------------
# CLASE mago (hereda de personaje)
# ------------------------------------------------------------
class mago(personaje):
    """
    Clase que representa a un mago.
    Su daño depende de la inteligencia y del poder de su libro mágico.
    """

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, libro):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        self.libro = libro

    def atributos(self):
        """Muestra los atributos del mago."""
        super().atributos()
        print("°Libro:", self.libro)

    def damage(self, enemigo):
        """Daño basado en inteligencia y poder mágico."""
        daño = self.inteligencia * self.libro - enemigo.defensa
        return max(0, daño)

    def sound(self):
        """Sonido característico del mago."""
        print(" WOOOOSH ")


# ------------------------------------------------------------
# CLASE enemy_p (hereda de personaje)
# ------------------------------------------------------------
class enemy_p(personaje):
    """
    Clase para enemigos comunes.
    Pueden tener veneno (poison) y trucos especiales.
    """

    poison = 0
    truco = 0

    @classmethod
    def hemorragia(cls):
        """Activa el estado de veneno común."""
        cls.poison = 5

    @classmethod
    def trick(cls):
        """Activa el estado de truco común."""
        cls.truco = 5

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa, truco=None, poison=None):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)
        # Usa los valores de clase si no se pasan valores específicos
        self.truco = truco if truco is not None else enemy_p.truco
        self.poison = poison if poison is not None else enemy_p.poison

    def atributos(self):
        """Muestra los atributos del enemigo."""
        super().atributos()
        print("°Truco:", self.truco)
        print("°Veneno:", self.poison)

    def subir_nivel(self, fuerza, vida, defensa, inteligencia, truco=None, poison=None):
        """Aumenta atributos y añade mejoras a truco/veneno."""
        super().subir_nivel(fuerza, vida, defensa, inteligencia)
        self.truco += truco
        self.poison += poison

    def damage(self, enemigo):
        """Daño basado en truco y veneno."""
        daño = self.truco * self.poison - enemigo.defensa
        return max(0, daño)

    def sound(self):
        """Sonido del enemigo."""
        print("sssss")


# ------------------------------------------------------------
# CLASE unique (hereda de personaje)
# ------------------------------------------------------------
class unique(personaje):
    """
    Clase para personajes únicos.
    Ejemplo: criaturas especiales con comportamiento distinto.
    """

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)

    def atributos(self):
        """Usa la versión base del método atributos."""
        return super().atributos()

    def damage(self, enemigo):
        """Usa el cálculo de daño estándar."""
        daño = super().damage(enemigo)
        return max(0, daño)

    def dog_sound(self):
        """Sonido especial del personaje."""
        print("WOOF")

    def sound(self):
        """Método requerido por la clase abstracta."""
        pass


# ============================================================
# EJEMPLOS DE USO
# ============================================================

# Crear instancias de guerrero y mago
guts = guerrero("Guts", 20, 10, 100, 100, 5)
vanessa = mago("Violet", 5, 30, 50, 10, 5)

#guts.atributos()
#guts.walk()
#guts.sound()

# Crear enemigos
enemy_p.trick()
enemy_p.hemorragia()

#comun = enemy_p("common", 10, 0, 10, 5)
#comun.atributos()

#rare = enemy_p("rare", 30, 10, 30, 10)
#rare.subir_nivel(0, 0, 0, 0, 4, 10)
#rare.atributos()

# Ejemplo de ataque simple
#comun.atacar(guts)

# ------------------------------------------------------------
# FUNCIÓN combate()
# ------------------------------------------------------------
def combate(p1, p2):
    """
    Ejecuta una batalla entre dos personajes hasta que uno muere.
    Ambos se atacan por turnos y se muestran los resultados.
    """
    turno = 0
    while p1.esta_vivo() and p2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", p1.nombre, ":")
        p1.atacar(p2)
        print(">>> Acción de", p2.nombre, ":")
        p2.atacar(p1)
        turno += 1

    if p1.esta_vivo():
        print(f"\n{p1.nombre} gana")
    elif p2.esta_vivo():
        print(f"\n{p2.nombre} gana")
    else:
        print("\nEmpate")

# Simulación de combate
combate(guts, vanessa)

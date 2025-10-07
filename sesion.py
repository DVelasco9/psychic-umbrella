#class shark:
 #   def __init__(self, name, size, age):
  #      self.name = name            #PUBLIC ATTRIBUTE
   #    self.__age = age            #PRIVATE ATTRIBUTE
    

    #PUBLIC METHOD
   # def get_info(self):
    #    return f"name: {self.name}, Size: {self._size}, Age: {self.__age}"
    

    #def bark(self):
     
     #   print("WOOF")

    #GETTER AND SETTER FOR PRIVATE ATTRIBUTE
    #def get_age(self):
     #   return self.__age
    
    #def set_age(self, age):
    #    if age >= 0:
     #       self.__age = age
      #  else:
       #     print("invalid age")
        



#tigershark = shark("Tiburon", 2, 2)

#print(tigershark.name)
#print(tigershark._size)
#print(tigershark.get_age())

#tigershark.set_age(6)
#print(tigershark.get_info())

from abc import ABC, abstractmethod

#___________________Listas___________________
WorkersInfoBasica = []
PasantesInfoBasica = []

Aguinaldo = []

#______________________________________________________FUNCIONES_GENERALES________________________________________________________________________________________________
@staticmethod
def CalcularAguinaldo():                                                                                        # Método estático independiente de los datos
    print("Esta función es ajena a las listas locales, debe ser tomada únicamente cómo referencia y no cómo un cálculo oficial de la empresa")
    Salario = int(input("Ingresar el salario del trabajador por día: "))
    print(f"El aguinal correspondiente es de: {Salario * 15}")

def UbicarTrabajadores():                                                                                       # Muestra la información básica de todos los trabajadores
    print(WorkersInfoBasica)

def UbicarPasantes():                                                                                           # Muestra nombre y puesto de todos los pasantes
    print(PasantesInfoBasica)

#_____________________________________________________________________CLASS______________________________________________________________________________________________
class Worker(ABC):                # Class Name
    Empresa = "MDSeguros"         # Class Attributes

    def __init__(self, name, age, position): # Constructor
        self.name = name                     # Object Attribute
        self._age = age                      # Object Attribute
        self.position = position             # Object Attribute

        WorkersInfoBasica.append(f"El trabajador {self.name} se desempeña como {self.position}.")        # Añade el objeto a una lista
        WorkersInfoBasica.sort()                                                                         # Acomoda la lista alfabéticamente acorde al nombre

        #print(f"Añadiendo trabajador {name}")     # Message when creating an object
    
    #____________________________Misc____________________________
    def GoodMorning(self):                                                                     # Saludar al trabajador/pasante    
        print(f"¡Buenos días {self.name}!")

    def MostrarInfo(self):                                                                     # Mostrar información del trabajador
        return f"Nombre: {self.name} / Edad: {self._age} / Puesto: {self.position}"

    #____________________________Pagos____________________________
    def GetPaid(self):                                           # GetPaid method
        print("¡El trabajador ha recibido su pago!")             # GetPaid message is printed
    
    def AguinaldoRecibido(self):                                 # Marca a los trabajadores que recibieron su aguinaldo y después lo confirma
        Aguinaldo.append(self.name)
        print(f"{self.name} recibió su aguinaldo")
        print(f"Se ha otorgado aguinaldo este año a: {Aguinaldo}")
    
    #@abstractmethod
    def DarPrestamo(self):
        Prestamo = input("Introducir monto de préstamo: ")
        print(f"{self.name} con el puesto {self.position} ha pedido un préstamo por {Prestamo}")

    #____________________________Cambios_de_puesto_o_empresa____________________________

    def CambioDePuesto(self):                                                           # Ayuda a cambiar de puesto al trabajador seleccionado
        self.position = input(f"Puesto al que se moverá {self.name}: ")
        print(f"Guardado {self.position} con éxito.")

    @classmethod
    def CambiarEmpresaTodos(self):                                                      # Migra toda la plantilla de trabajadores a otra empresa
        Worker.Empresa = input("Empresa a traspasar trabajadores: ")
        print(f"Guardado {self.Empresa} con éxito.")
    
    #____________________________Despido____________________________
    def Despedido(self):
        print(f"El trabajador {self.name} a culminado su estancia laboral en esta empresa.")      # Despide a un trabajador con una nota en su historial
        Culminar = input("¿Fué renuncia voluntaria? [Y = 1/N = 0]: ")
        if Culminar == "1":
            self.position = "Renuncia"
        elif Culminar == "0":
            self.position = "Despedido/No recontratar"
        else:
            print("Reinicie el programa e introduzca un dígito válido.")
    
    @abstractmethod
    def SellarPracticas(self):                                                                    # Método exclusivo de subclase Pasantes
        pass

    def SellarPracticas(self):
        pass

    
#_________PASANTE__________________________________________________________________PASANTE_________________________________________________________________________
class Pasante(Worker):

    def __init__(self, name, age, position, school): # Constructor
        self.name = name
        self._age = age
        self.position = position
        self.__school = school

        PasantesInfoBasica.append(f"El pasante {self.name} se desempeña como {self.position}.")    # Añade el objeto a una lista
        PasantesInfoBasica.sort()                                                                  # Y la acomoda alfabéticamente

        print(f"Se ha añadido al pasante {self.name}")
    
    #____________________________MISC_____________________________
    def MostrarInfo(self):                                                                                          # Muestra toda la info del objeto
        return f"Nombre: {self.name} / Edad: {self._age} / Puesto: {self.position} / Escuela: {self.__school}"
    
    #____________________________Pagos____________________________
    def GetPaid(self):                                                                                              # Advierte de que el pasante no recibe sueldo
        print("El pasante no está autorizado a recibir pago remunerado, consulte administración.")
    
    def AguinaldoRecibido(self):                                                                                    # Advierte que el pasante no recibe aguinaldo
        print("El pasante no está autorizado a recibir aguinaldo, consulte con administración")
    
    #@abstractmethod
    #def DarPrestamo():
    #    print("El pasante no puede recibir préstamos")

    #____________________________Culminación____________________________

    def Despedido(self):                                                                                            # Culmina la relación con el pasante
        print(f"El pasante {self.name} no ha culminado con exito sus pasantías. Notificar a {self.__school}.")
        self.position = "No contratar en el futuro"
    
    def SellarPracticas(self):                                                                                      # Marca la finalización del periodo de practicas
        print(f"El pasante {self.name} ha culminado sus prácticas.")
        self.position = "Pasantía terminada"

#__________________________________ACTIONS____________________________________ACTIONS____________________________ACTIONS____________________________________

Worker1 = Worker("Luis", 19, "Almacenista")                                                             # Constructor en acción
Worker2 = Worker("Bonifacio", 25, "Recepcionista")
Worker3 = Worker("Laura", 21, "Recursos Humanos")
Pasante1 = Pasante("Lautaro", 18, "Asistente recursos humanos", "UAN")
Pasante2 = Pasante("Pepe", 21, "Asistente Almacen", "UPEN")
Pasante3 = Pasante("Avdul", 22, "Asistente de recepción", "UAN")
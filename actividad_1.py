class shark:                    #CLASS NAME EL NOMBRE DE CLASE DEBERIA SER ANIMAL, PERO COMO HAY QUE REHACER VARIAS PARTES DEL CODIGO, ENTONCES ASI SE QUEDA
    species = " "   #CLASS ATTRIBUTE

    def __init__(self):                  #CONSTRUCTOR
       # while True:
        #    try:
         #       cantidad = int(input("Cantidad de animales que quiera crear? "))
          #      break
           # except ValueError:
            #    print("intente de nuevo")

       # for  = cantidad:
        while True:
            try:
                self.age = int(input(f"Introduzca la edad de su {shark.species}: "))  #OBJECT ATTRIBUTE
                break
            except ValueError:
                print("Parece que colocó letras, intente de nuevo")                           
        
        while True:
            try:
                 self.size = float(input(f"Introduzca el tamaño de su {shark.species}: "))  #OBJECT ATTRIBUTE
                 break   
            except ValueError:
                print("Parece que no colocó letras, vuelva a intentarlo")                       


        
        print("creating a new animal")               #A MESSAGE APPEARS WHEN CREATING AN OBJECT
        print(f"el objeto {shark.species} con los atributos\nedad: {self.age}\ntamaño: {self.size}\nha sido creado")            #A FEEDBACK OF WHAT HAPPENED WITH ATTRIBUTES


    @staticmethod
    def bite():             #BITE METHOD
        print("ñam")            #A BITE MESSAGE IS PRINTED 

    def change_class(self):
        self.species = "Dolphin"
    
    @classmethod
    def change_species(shark):
        while True:
            new_species = input("Which species do you want or animal, whatever? ")
            if new_species.isalpha():
                print("")
                break
            else:
                print("entrada de nombre invalido, vuelva a intentarlo")
            
        shark.species = new_species
        
class tigershark(shark):
    methabolism = "High"
    
    def trasheater():
        print("The sharks has eaten over 1KG of ocean trash")

class dogs():
    def bark(self):
        print("woof")


shark.change_species()


shark1 = shark()
shark1.bite()

shark2 = shark()

shark3 = shark()


shark4 = tigershark()
shark4.bite
shark4.trasheater
print(f"The methabolism of this shark is {shark4.methabolism}")
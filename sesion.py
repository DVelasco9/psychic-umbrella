class dog: 
    species = "Canine" #CLASS ATTRIBUTE

    def __init__(self, name, age): #constructor
        self.name = name           #OBJECT ATTRIBUTE
        self.age = age             #OBJECT ATTRIBUTE


        print(f"Creating new object {name}")

    def bark(self):
        print("WOOF")




dog1 = dog("Scooby",14)
dog2 = dog("solovino",2)

dog1.bark()

print(dog1.bark)
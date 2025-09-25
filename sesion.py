class shark:
    def __init__(self, name, size, age):
        self.name = name            #PUBLIC ATTRIBUTE
        self._size = size           #PROTECTED ATTRIBUTE
        self.__age = age            #PRIVATE ATTRIBUTE
    

    #PUBLIC METHOD
    def get_info(self):
        return f"name: {self.name}, Size: {self._size}, Age: {self.__age}"
    

    def bark(self):
        print("WOOF")

    #GETTER AND SETTER FOR PRIVATE ATTRIBUTE
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("invalid age")
        



tigershark = shark("Tiburon", 2, 2)

print(tigershark.name)
print(tigershark._size)
print(tigershark.get_age())

tigershark.set_age(6)
print(tigershark.get_info())


tigershark.bark()


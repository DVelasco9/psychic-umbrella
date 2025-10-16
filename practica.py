from abc import ABC, abstractmethod

user = input("Figura geometrica que quiere calcular: ")

class figura_geometrica(ABC):
    height = 0
    base = 0

    def __init__(self, height=None, base=None):
        self.height = height
        self.base = base
        
    def infores(self):
        print("-"*40)
        print(f"""Datos:
        base {self.base} metros
        altura {self.height} metros""")
        print("-"*40)

    @abstractmethod
    def perimetro(self):
        pass

    @staticmethod
    def proceso():
        print("Calculando area y perimetro")

class square(figura_geometrica):
    def __init__(self, height, base, lado):
        lado = float(input("Coloque la medida del lado (metros): "))
        super().__init__(height, base)
        self.lado = lado

    def infores(self):
        super().infores()
        print(f"""°Lado: {self.lado} metros
El area del cuadrado es igual a {self.lado * self.lado} metros""")
        print("-"*40)

    def perimetro(self):
        print(f"El perimetro es igual a {self.lado*4} metros")
        print("-"*40)
            
class triangulo(figura_geometrica):
    def __init__(self, height=None, base=None):
        super().__init__(height, base)
        base = float(input("Medida de la base del triángulo? "))
        height = float(input("Medida de la altura del triángulo? "))
        self.base = base
        self.height = height

    def infores(self):
        super().infores()
        print(f"""El area es igual a {(self.base * self.height)/2}""")
        print("-"*40)
        
    
    def perimetro(self):
        print("-"*40)
        print(f"El perimetro es igual a {self.base + self.height + self.height}")

class rectangulo(figura_geometrica):
    def __init__(self, height=None, base=None):
        super().__init__(height, base)
        base = float(input("Medida de la base del rectángulo? "))
        height = float(input("Medida de la altura del rectángulo? "))
        self.base = base
        self.height = height
    
    def infores(self):
        super().infores()
        print(f"el área es igual a {self.base * self.height} metros")
        print("-"*40)

    def perimetro(self):
        print(f"El perimetro es igual a {(self.base * 2) + (self.height * 2)} metros")

if user.lower() in ("cuadrado", "c"): 
    c = square(0,0,0)
    c.proceso()
    c.perimetro()
    c.infores()
elif user.lower() in ("triangulo", "t", "triángulo"):
    t = triangulo(0,0)
    t.proceso()
    t.perimetro()
    t.infores()
elif user.lower() in ("rectangulo", "r", "rectángulo"):
    r= rectangulo(0,0)
    r.proceso()
    r.infores()
    r.perimetro()
else:
    print("FIGURA EN PROCESO DE CONSTRUCCIÓN")

# Importación de módulos necesarios
from abc import ABC, abstractmethod  # ABC para clases abstractas, abstractmethod para métodos abstractos
import re  # Para expresiones regulares (validación de email)

# Clase abstracta Employee que define la estructura base para todos los empleados
class Employee(ABC):
  # Variables de clase
  _company_status = "Active"  # Atributo protegido con el estado de la compañía
  role = "Employee"  # Rol por defecto

  # Constructor de la clase
  def __init__(self, name, age, email, employee_id):
    self.name = name  # Atributo público
    self.age = age  # Atributo público
    self._email = email  # Atributo protegido
    self.__employee_id = employee_id  # Atributo privado
    self.__salary_paid = False  # Atributo privado

  # Método para saludar
  def salute(self):
    print(f'Hello! I am {self.name}, your {self.role.lower()}')

  # Método para mostrar información del empleado
  def view_info(self):
    print(f"""Employee Information:
  ID: {self.__employee_id} 
  Name: {self.name}
  Age: {self.age}
  Email: {self._email}
  Role: {self.role} 
  Status: {self._company_status}""")

  # Obtener el ID del empleado (atributo privado)
  def get_employee_id(self):
    print(f"ID: {self.__employee_id}")

  # Setter para el email
  def set_email(self):
    self._email = input(f"Set a new email for {self.name}: ")
    print(f"New email: {self._email}")

  # Método de clase para cambiar el estado de la compañía
  @classmethod
  def change_company_status(cls):
    cls._company_status = input("Set a new company status: ")
    print(f"Company status changed to: {cls._company_status}")

  # Método estático para validar formato de email
  @staticmethod
  def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Patrón regex para email
    print(f"The email: {email} is it valid? {re.match(pattern, email) is not None}")

  # Método abstracto que debe ser implementado por las clases hijas
  @abstractmethod
  def work(self):
    pass

  # Método para marcar el salario como pagado
  def pay_salary(self):
    self.__salary_paid = True
    print(f"Salary paid successfully to {self.name}")


# Clase Developer que hereda de Employee
class Developer(Employee):
  team = "Development"  # Variable de clase específica para desarrolladores
  _base_salary = 20000  # Salario base protegido

  # Constructor que extiende al del padre
  def __init__(self, name, age, email, employee_id, programming_language):
    super().__init__(name, age, email, employee_id)  # Llamada al constructor del padre
    self.role = "Developer"  # Sobrescribe el rol
    self.programming_language = programming_language  # Atributo específico

  # Implementación del método abstracto work
  def work(self):
    print(f"  - {self.name} is developing software in {self.programming_language}")

  # Método para mostrar el salario
  def salary(self):
    print(f"  - {self.name}'s salary: ${self._base_salary}")

  # Extiende el método view_info del padre
  def view_info(self):
    super().view_info()  # Llama al método del padre
    print(f"  Programming Language: {self.programming_language}")
    print(f"  Team: {self.team}")


# Clase GraphicDesigner que hereda de Employee
class GraphicDesigner(Employee):
  team = "Creative"  # Variable de clase específica para diseñadores
  _base_salary = 15000  # Salario base

  def __init__(self, name, age, email, employee_id, design_tool):
    super().__init__(name, age, email, employee_id)
    self.role = "Graphic Designer"
    self.design_tool = design_tool  # Herramienta de diseño específica

  # Método abstracto work
  def work(self):
    print(f"  - {self.name} is creating designs using {self.design_tool}")

  # Método específico de diseñadores gráficos
  def create_prototype(self):
    print(f"{self.name} is creating a design prototype...")

  def salary(self):
    print(f"  - {self.name}'s salary: ${self._base_salary}")

  # Extiende el método view_info del padre
  def view_info(self):
    super().view_info() # Llama al método del padre
    print(f"  Design Tool: {self.design_tool}")
    print(f"  Team: {self.team}")


# Clase SeniorDeveloper que hereda de Developer
class SeniorDeveloper(Developer):
  def __init__(self, name, age, email, employee_id, programming_language, years_experience):
    super().__init__(name, age, email, employee_id, programming_language)
    self.role = "Senior Developer"
    self.years_experience = years_experience  # Años de experiencia específicos

  def salary(self):
    print(f"  - {self.name}'s salary: ${self._base_salary}")

  # Método específico para senior developers
  def mentor_junior(self):
    print(f"{self.name} is mentoring junior developers...")

  # Extiende el método view_info del padre
  def view_info(self):
    super().view_info() # Llama al método del padre
    print(f"  Years experience: {self.years_experience}")


# === Creación de objetos === #
dev1 = Developer("Abdiel", 25, "abdiel@company.com", 1001, "Python")
dev2 = Developer("Níz", 20, "niz@company.com", 1004, "JavaScript")
designer1 = GraphicDesigner("Maria", 28, "maria@company.com", 1002, "Figma")
senior_dev = SeniorDeveloper("Diego", 32, "diego@company.com", 1003, "Java", 8)


# === Ejecución y demostración === #
employees = [dev1, dev2, designer1, senior_dev]  # Lista con todos los empleados

print("People chambianding:")  # Probablemente quería decir "working" o "changing"
for emp in employees:
  emp.work()  # Polimorfismo: cada empleado ejecuta su propia versión de work()
print("-" * 40)

print("View email:")
for emp in employees:
  print(f"  - {emp.name}'s email: {emp._email}")  # Accediendo a atributo protegido
print("-" * 40)

# Cambiar email y validarlo
dev1.set_email()
Employee.validate_email(dev1._email)

print("-" * 40)
print("Employee salaries:")
for emp in employees:
  emp.salary()  # Cada empleado muestra su salario
print("-" * 40)

# Pagar salarios a todos los empleados
for emp in employees:
  emp.pay_salary()
print("-" * 40)

# Mostrar información completa de cada empleado
for emp in employees:
  emp.view_info()
  print("-" * 40)

# Métodos específicos de cada clase
designer1.create_prototype()
senior_dev.mentor_junior()
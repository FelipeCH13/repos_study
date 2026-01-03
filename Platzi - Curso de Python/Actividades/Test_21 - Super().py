# Declaracion clase Persona
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f"Hello! I am a Persona.")

# Declaracion clase Student que hereda de Persona
class Student(Persona):
    # Constructor de la clase Student
    def __init__(self, name, age, student_id):
        # Llamada al constructor de la clase base
        super().__init__(name, age)
        self.student_id = student_id

    def saludar(self):
        super().saludar()
        print(f"Hello, my student ID is {self.student_id}.")

# Ejemplo de uso
student1 = Student("Alice", 20, "S12345")
student1.saludar()


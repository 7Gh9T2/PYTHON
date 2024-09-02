from abc import ABC, abstractmethod

class Persona(ABC):
    """Clase que representa una persona."""

    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def __str__(self):
        return "Persona: %s, %s, %s" % (str(self.cedula), self.apellido, self.nombre)

class Alumno(Persona):
    """Clase que representa a un alumno."""

    def __init__(self, cedula, nombre, apellido, carrera):
        # Llamamos al constructor de Persona
        Persona.__init__(self, cedula, nombre, apellido)
        # Agregamos el nuevo atributo
        self.carrera = carrera

    def __str__(self):
        return "Alumno: %s, %s, %s, %s" % (self.cedula, self.nombre, self.apellido, self.carrera)

if __name__ == "__main__":
   
    alumno = Alumno("4553788", "Marcos", "Rios", "Ingeniería")
    
    print(alumno)
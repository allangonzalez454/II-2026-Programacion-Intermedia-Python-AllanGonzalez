from Persona import Persona

class Estudiante(Persona): 

    def __init__(self, nombre, identificacion, carrera):
        super().__init__(nombre, identificacion)
        self.carrera = carrera

    def obtener_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")
        print(f"Carrera: {self.carrera}")
from persona import Persona
class Profesor(Persona):
    def __init__(self, nombre, identificacion, departamento):
        super().__init__(nombre, identificacion)
        self.departamento = departamento

    def obtener_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")
        print(f"Departamento: {self.departamento}")
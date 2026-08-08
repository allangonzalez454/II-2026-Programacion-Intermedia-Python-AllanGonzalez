class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def obtener_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")
        
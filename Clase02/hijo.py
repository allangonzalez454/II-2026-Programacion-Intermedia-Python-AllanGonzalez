class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def obtener_detalles(self):
        return f"Nombre: {self.nombre}, Identificación: {self.identificacion}"


class Estudiante(Persona):
    def __init__(self, nombre, identificacion, carrera):
        super().__init__(nombre, identificacion)
        self.carrera = carrera

    def obtener_detalles(self):
        return f"{super().obtener_detalles()}, Carrera: {self.carrera}"


class Profesor(Persona):
    def __init__(self, nombre, identificacion, departamento):
        super().__init__(nombre, identificacion)
        self.departamento = departamento

    def obtener_detalles(self):
        return f"{super().obtener_detalles()}, Departamento: {self.departamento}"


def imprimir_detalles(persona):
    print(persona.obtener_detalles())


if __name__ == "__main__":
    estudiante1 = Estudiante("Ana Rojas", "1-1234-5678", "Ingeniería en Sistemas")
    estudiante2 = Estudiante("Luis Mora", "2-2345-6789", "Administración")
    profesor1 = Profesor("Carla Solano", "3-3456-7890", "Matemáticas")
    profesor2 = Profesor("Jorge Vargas", "4-4567-8901", "Informática")

    personas = [estudiante1, estudiante2, profesor1, profesor2]

    for persona in personas:
        imprimir_detalles(persona)
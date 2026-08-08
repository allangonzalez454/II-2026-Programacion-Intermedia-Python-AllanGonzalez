from clase02 import Usuario

class Administrador(Usuario):
    def __init__(self, username, password, email, nombre="", apellido="", direccion="", edad=0):
        super().__init__(username, password, email, nombre, apellido, direccion, edad)
        self.usuarios = [] 



    super().__init__(username, password, email, nombre, apellido, direccion, edad)

def agregar_usuario(self, usuario):
    self.usuarios.append(usuario)

def eliminar_usuario(self, usuario):
    if usuario in self.usuarios:
        self.usuarios.remove(usuario)
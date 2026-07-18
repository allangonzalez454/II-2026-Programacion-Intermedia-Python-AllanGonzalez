class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.año_publicacion}"
    
    
class Pelicula:
    def _init_(self, titulo, genero, duracion, presupuesto, calificacion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.presupuesto = presupuesto
        self.calificacion = calificacion 

    def mostrar_datos(self):
        print("Título:", self.titulo)
        print("Género:", self.genero)
        print("Duración:", self.duracion)
        print("Presupuesto:", self.presupuesto)
        print("Calificación:", self.calificacion)



peliculas = []

pelicula_1 = Pelicula("Odisea", "Ficción", 3, 250_000_000, 10)
pelicula_2 = Pelicula("Spiderman", "Ficción", 2, 100_000_000, 9)
pelicula_3 = Pelicula("Pulp Fiction", "Acción", 2, 2_000_000, 10)
pelicula_4 = Pelicula("Abril", "Drama", 1.30, 500_000, 8)
pelicula_5 = Pelicula("Batman", "Ficción", 2.30, 30_000_000, 9)

peliculas.extend([pelicula_1, pelicula_2, pelicula_3, pelicula_4, pelicula_5])
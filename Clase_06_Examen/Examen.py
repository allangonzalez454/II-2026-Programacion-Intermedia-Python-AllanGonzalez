class Pelicula:
    def __init__(self, titulo, genero, duracion, presupuesto, calificacion):
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

for peli in peliculas:
    peli.mostrar_datos()
    print("-" * 30)

    import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "titulo": [p.titulo for p in peliculas],
    "genero": [p.genero for p in peliculas],
    "duracion": [p.duracion for p in peliculas],
    "presupuesto": [p.presupuesto for p in peliculas],
    "calificacion": [p.calificacion for p in peliculas]
}

df = pd.DataFrame(datos)

print(df)

df.info()

print("Promedio de duración:", df["duracion"].mean())
print("Promedio de presupuesto:", df["presupuesto"].mean())
print("Promedio de calificación:", df["calificacion"].mean())

print("Mayor duración:", df["duracion"].max())
print("Menor duración:", df["duracion"].min())

correlacion = df.corr(numeric_only=True)
print(correlacion)

print("Correlación Duración vs Calificación:", correlacion.loc["duracion", "calificacion"])
print("Correlación Presupuesto vs Calificación:", correlacion.loc["presupuesto", "calificacion"])

plt.scatter(df["presupuesto"], df["calificacion"])
plt.xlabel("Presupuesto")
plt.ylabel("Calificación")
plt.title("Presupuesto vs Calificación")
plt.show()
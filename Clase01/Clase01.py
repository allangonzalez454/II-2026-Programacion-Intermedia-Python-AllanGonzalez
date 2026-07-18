from .Libro import Libro

opcion = 0 
libros = {}

while opcion != 3:
    print("menu:")
    print("1. Crear un libro")
    print("2. Mostrar libro")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año_publicacion = int(input("Ingrese el año de publicación del libro: "))
        libro = Libro(titulo, autor, año_publicacion)
        libros[titulo] = libro
        print(f"Libro '{titulo}' creado exitosamente.")
    elif opcion == 2:
        titulo = input("Ingrese el título del libro que desea mostrar: ")
        libro = libros[titulo]
        print(libro)
from Libro import Libro

opcion = ""
libros = {}

while opcion != "3":
    print("menu:")
    print("1. Crear un libro")
    print("2. Mostrar libro")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año_publicacion = input("Ingrese el año de publicación del libro: ")
        if not año_publicacion.isdigit():
            print("El año debe ser un número.")
            continue
        libro = Libro(titulo, autor, año_publicacion)
        libros[titulo] = libro
        print(f"Libro '{titulo}' creado exitosamente.")
    elif opcion == "2":
        titulo = input("Ingrese el título del libro que desea mostrar: ")
        if titulo in libros:
            print(libros[titulo])
        else:
            print("Libro no encontrado.")
    elif opcion != "3":
        print("Opción inválida.")
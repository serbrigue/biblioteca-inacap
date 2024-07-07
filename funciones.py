import json
import os

# Pausa la ejecución hasta que el usuario presione enter y luego limpia la pantalla.
def congelar():
    input('Presione enter para continuar...')
    os.system('clear')

# Abre un archivo JSON y devuelve su contenido como una lista de diccionarios.
# Si el archivo no existe, retorna una lista vacía.
def abrir(archivo):
    try:
        with open(archivo, 'r') as file:
            productos_data = file.read().strip()
            if not productos_data:
                return []
            return json.loads(productos_data)
    except FileNotFoundError:
        print('Error: Archivo no encontrado')
        return []

# Guarda una lista de diccionarios en un archivo JSON.
def guardar(archivo, libros):
    try:
        with open(archivo, 'w') as file:
            libros_data = json.dumps(libros, indent=4)
            file.write(libros_data)
    except Exception as e:
        print(f'Error al guardar archivo: {e}')

# Busca un libro por su título en la lista de libros.
# Si encuentra el libro, lo devuelve; si no, devuelve None.
def buscar(nombre_libro, archivo):
    for libro in archivo:
        if libro["titulo"] == nombre_libro:
            return libro
    return None

# Agrega un libro a la lista de libros.
# Verifica que el año de publicación sea un número positivo.
# Si el libro ya existe, muestra un mensaje de error.
def agregar(titulo, autor, fecha, archivo):
    try:
        fecha = int(fecha)
        if fecha <= 0:
            raise ValueError('Fecha debe ser un número positivo')
    except ValueError as e:
        return f'Error: {e}'

    if buscar(titulo, archivo):
        return "Error: Libro ya existe"
    else:
        archivo.append({"titulo": titulo, "autor": autor, "fecha": fecha})
        guardar("libros.json", archivo)
        return 'Libro agregado exitosamente'

# Modifica la información de un libro existente.
# Verifica que el año de publicación sea un número positivo.
# Si el libro no existe, muestra un mensaje de error.
def modificar(titulo, nuevo_autor, nueva_fecha, archivo):
    libro = buscar(titulo, archivo)
    if libro:
        try:
            nueva_fecha = int(nueva_fecha)
            if nueva_fecha <= 0:
                raise ValueError('Fecha debe ser un número positivo')
        except ValueError as e:
            return f'Error: {e}'

        libro["autor"] = nuevo_autor
        libro["fecha"] = nueva_fecha
        guardar("libros.json", archivo)
        return 'Libro modificado exitosamente'
    else:
        return "Error: Libro no encontrado"

# Muestra todos los libros en la lista de libros.
# Si no hay libros, muestra un mensaje indicando que la lista está vacía.
def mostrar(archivo):
    if len(archivo) == 0:
        return "No hay libros en la librería"
    
    resultado = ""
    for i, libro in enumerate(archivo):
        resultado += f'{i+1}. Titulo: {libro["titulo"]} - Autor: {libro["autor"]} - Publicacion: {libro["fecha"]}\n'
    
    return resultado.strip()

# Elimina un libro de la lista de libros.
# Si el libro no existe, muestra un mensaje de error.
def eliminar(titulo, archivo):
    libro = buscar(titulo, archivo)
    if libro:
        archivo.remove(libro)
        guardar("libros.json", archivo)
        return 'Libro eliminado exitosamente'
    else:
        return "Error: Libro no encontrado"

# Menú interactivo para la gestión de libros en la biblioteca.
# Permite agregar, modificar, buscar, mostrar y eliminar libros, además de salir del programa.
def menu():
    libros = abrir("libros.json")
    while True:
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Buscar libro")
        print("4. Mostrar libros")
        print("5. Eliminar libro")
        print("6. Salir")
        
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error: Ingrese un número válido")
            continue

        if opcion == 1:
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            fecha = input("Ingrese la fecha del libro: ")
            print(agregar(titulo, autor, fecha, libros))
            congelar()
        elif opcion == 2:
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el nuevo autor para el libro: ")
            fecha = input("Ingrese la nueva fecha para el libro: ")
            print(modificar(titulo, autor, fecha, libros))
            congelar()
        elif opcion == 3:
            titulo = input("Ingrese el titulo del libro: ")
            libro = buscar(titulo, libros)
            if libro:
                print(f'Titulo: {libro["titulo"]} - Publicación: {libro["fecha"]} - Autor: {libro["autor"]}')
            else:
                print('Error: Libro no encontrado')
            congelar()
        elif opcion == 4:
            print(mostrar(libros))
            congelar()
        elif opcion == 5:
            titulo = input("Ingrese el titulo del libro: ")
            print(eliminar(titulo, libros))
            congelar()
        elif opcion == 6:
            guardar("libros.json", libros)
            print("Adios")
            break
        else:
            print("Error: Opción no válida")





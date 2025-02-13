import json
import os

# Pausa la ejecución hasta que el usuario presione enter y luego limpia la pantalla.
def pausar_ejecucion():
    input('Presione enter para continuar...')
    os.system('clear')

# Verifica si la lista de libros está vacía.
def verificar(archivo):
    return len(archivo) == 0

# Abre un archivo JSON y devuelve su contenido como una lista de diccionarios.
# Si el archivo no existe, retorna una lista vacía.
def abrir_archivo(archivo):
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
def guardar_archivo(archivo, libros):
    try:
        with open(archivo, 'w') as file:
            libros_data = json.dumps(libros, indent=4)
            file.write(libros_data)
    except Exception as e:
        print(f'Error al guardar archivo: {e}')

# Busca un libro por su título en la lista de libros.
# Si encuentra el libro, lo devuelve; si no, devuelve None.
def buscar_libro(nombre_libro, archivo):
    for libro in archivo:
        if libro["titulo"] == nombre_libro:
            return libro
    return None

# Agrega un libro a la lista de libros.
# Verifica que el año de publicación sea un número positivo.
# Si el libro ya existe, muestra un mensaje de error.
def agregar_libro(titulo, autor, fecha, archivo):
    try:
        fecha = int(fecha)
        if fecha <= 0:
            raise ValueError('Fecha debe ser un número positivo')
    except ValueError as e:
        return f'Error: {e}'

    if buscar_libro(titulo, archivo):
        return "Error: Libro ya existe"
    else:
        archivo.append({"titulo": titulo, "autor": autor, "fecha": fecha})
        guardar_archivo("libros.json", archivo)
        return 'Libro agregado exitosamente'

# Modifica la información de un libro existente.
# Verifica que el año de publicación sea un número positivo.
# Si el libro no existe, muestra un mensaje de error.
def modificar_libro(titulo, nuevo_autor, nueva_fecha, archivo):
    libro = buscar_libro(titulo, archivo)
    if libro:
        try:
            nueva_fecha = int(nueva_fecha)
            if nueva_fecha <= 0:
                raise ValueError('Fecha debe ser un número positivo')
        except ValueError as e:
            return f'Error: {e}'

        libro["autor"] = nuevo_autor
        libro["fecha"] = nueva_fecha
        guardar_archivo("libros.json", archivo)
        return 'Libro modificado exitosamente'
    else:
        return "Error: Libro no encontrado"

# Muestra todos los libros en la lista de libros.
# Si no hay libros, muestra un mensaje indicando que la lista está vacía.
def mostrar_libros(archivo):
    if verificar(archivo):
        return 'No hay libros en la biblioteca'
    else:
        resultado = ''
        for i, libro in enumerate(archivo):
            resultado += f'{i+1}. Titulo: {libro["titulo"]} - Autor: {libro["autor"]} - Publicacion: {libro["fecha"]}\n'
        return resultado.strip()

# Elimina un libro de la lista de libros.
# Si el libro no existe, muestra un mensaje de error.
def eliminar_libro(titulo, archivo):
    libro = buscar_libro(titulo, archivo)
    if libro:
        archivo.remove(libro)
        guardar_archivo("libros.json", archivo)
        return 'Libro eliminado exitosamente'
    else:
        return "Error: Libro no encontrado"

# Menú interactivo para la gestión de libros en la biblioteca.
# Permite agregar, modificar, buscar, mostrar y eliminar libros, además de salir del programa.
def menu():
    libros = abrir_archivo("libros.json")
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
            print(agregar_libro(titulo, autor, fecha, libros))
            pausar_ejecucion()
        elif opcion == 2:
            if verificar(libros):
                print('Error: No hay libros en la biblioteca')
            else:
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el nuevo autor para el libro: ")
                fecha = input("Ingrese la nueva fecha para el libro: ")
                print(modificar_libro(titulo, autor, fecha, libros))
            pausar_ejecucion()
        elif opcion == 3:
            if verificar(libros):
                print('Error: No hay libros en la biblioteca')
            else:
                titulo = input("Ingrese el titulo del libro: ")
                libro = buscar_libro(titulo, libros)
                if libro:
                    print(f'Titulo: {libro["titulo"]} - Publicación: {libro["fecha"]} - Autor: {libro["autor"]}')
                else:
                    print('Error: Libro no encontrado')
            pausar_ejecucion()
        elif opcion == 4:
            if verificar(libros):
                print('Error: No hay libros en la biblioteca')
            else:
                print(mostrar_libros(libros))
            pausar_ejecucion()
        elif opcion == 5:
            if verificar(libros):
                print('Error: No hay libros en la biblioteca')
            else:
                titulo = input("Ingrese el titulo del libro: ")
                print(eliminar_libro(titulo, libros))
            pausar_ejecucion()
        elif opcion == 6:
            guardar_archivo("libros.json", libros)
            print("Adios")
            break
        else:
            print("Error: Opción no válida")




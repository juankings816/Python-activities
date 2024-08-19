import os

class Tarea:
    def __init__(self, titulo, descripcion, estado='pendiente'):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __repr__(self):
        return f'Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def agregar_tarea(lista_tareas):
    try:
        titulo = input('Introduce el título de la tarea: ')
        descripcion = input('Introduce la descripción de la tarea: ')
        tarea = Tarea(titulo, descripcion)
        lista_tareas.append(tarea)
        print('Tarea agregada exitosamente.')
    except Exception as err:
        print(f'Error al agregar la tarea: {err}')
    input("\nPresiona Enter para continuar...")

def mostrar_tareas(lista_tareas):
    if lista_tareas:
        for tarea in lista_tareas:
            print(tarea)
            print('-' * 20)
    else:
        print('No hay tareas en la lista.')
    input("\nPresiona Enter para continuar...")

def buscar_tarea(lista_tareas):
    try:
        titulo_buscar = input('Introduce el título de la tarea a buscar: ').strip().lower()
        encontrada = next((tarea for tarea in lista_tareas if tarea.titulo.lower() == titulo_buscar), None)
        if encontrada:
            print(encontrada)
        else:
            print('Tarea no encontrada.')
    except Exception as err:
        print(f'Error al buscar la tarea: {err}')
    input("\nPresiona Enter para continuar...")

def actualizar_estado_tarea(lista_tareas):
    try:
        titulo_actualizar = input('Introduce el título de la tarea a actualizar: ').strip().lower()
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo_actualizar:
                tarea.estado = 'completada'
                print('Tarea actualizada a completada.')
                return
        print('Tarea no encontrada.')
    except Exception as err:
        print(f'Error al actualizar la tarea: {err}')
    input("\nPresiona Enter para continuar...")

def eliminar_tarea(lista_tareas):
    try:
        titulo_eliminar = input('Introduce el título de la tarea a eliminar: ').strip().lower()
        lista_tareas[:] = [tarea for tarea in lista_tareas if tarea.titulo.lower() != titulo_eliminar]
        if len(lista_tareas):
            print('Tarea eliminada.')
        else:
            print('Tarea no encontrada.')
    except Exception as err:
        print(f'Error al eliminar la tarea: {err}')
    input("\nPresiona Enter para continuar...")

def menu_principal():
    lista_tareas = []
    opciones = {
        1: agregar_tarea,
        2: mostrar_tareas,
        3: buscar_tarea,
        4: actualizar_estado_tarea,
        5: eliminar_tarea
    }
    while True:
        limpiar_pantalla()
        print('\nAdministrador de Tareas')
        print('1. Agregar tarea')
        print('2. Mostrar todas las tareas')
        print('3. Buscar tarea por título')
        print('4. Actualizar estado de tarea')
        print('5. Eliminar tarea por título')
        print('6. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion](lista_tareas)
            elif opcion == 6:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')
            input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    menu_principal()

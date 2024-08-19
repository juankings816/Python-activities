import os

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return f'Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def agregar_contacto(contactos):
    try:
        nombre = input('Introduce el nombre del contacto: ')
        telefono = input('Introduce el celular del contacto: ')
        email = input('Introduce el email del contacto: ')
        contacto = Contacto(nombre, telefono, email)
        contactos.append(contacto)
        print('Contacto agregado exitosamente.')
    except Exception as e:
        print(f'Error al agregar el contacto: {e}')
    input("\nPresiona Enter para continuar...")

def mostrar_contactos(contactos):
    if not contactos:
        print('No hay contactos en la lista.')
    else:
        for contacto in contactos:
            print(contacto)
            print('-' * 20)
    input("\nPresiona Enter para continuar...")

def buscar_contacto(contactos):
    try:
        nombre_buscar = input('Introduce el nombre del contacto a buscar: ').lower().strip()
        encontrado = next((contacto for contacto in contactos if contacto.nombre.lower() == nombre_buscar), None)
        if encontrado:
            print(encontrado)
        else:
            print('Contacto no encontrado.')
    except Exception as e:
        print(f'Error al buscar el contacto: {e}')
    input("\nPresiona Enter para continuar...")

def eliminar_contacto(contactos):
    try:
        nombre_eliminar = input('Introduce el nombre del contacto a eliminar: ').lower().strip()
        contactos[:] = [contacto for contacto in contactos if contacto.nombre.lower() != nombre_eliminar]
        print('Contacto eliminado.') if any(contacto.nombre.lower() == nombre_eliminar for contacto in contactos) else print('Contacto no encontrado.')
    except Exception as e:
        print(f'Error al eliminar el contacto: {e}')
    input("\nPresiona Enter para continuar...")

def menu_contactos():
    contactos = []
    opciones = {
        1: agregar_contacto,
        2: mostrar_contactos,
        3: buscar_contacto,
        4: eliminar_contacto
    }
    while True:
        limpiar_pantalla()
        print('\nGestión de Contactos')
        print('1. Agregar contacto')
        print('2. Mostrar todos los contactos')
        print('3. Buscar contacto por nombre')
        print('4. Eliminar contacto por nombre')
        print('5. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion](contactos)
            elif opcion == 5:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')
            input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    menu_contactos()

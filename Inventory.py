import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f'Nombre: {self.nombre}\nCantidad: {self.cantidad}\nPrecio: {self.precio}'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def agregar_producto(inventario):
    try:
        nombre = input('Introduce el nombre del producto: ')
        cantidad = int(input('Introduce la cantidad del producto: '))
        precio = float(input('Introduce el precio del producto: '))
        producto = Producto(nombre, cantidad, precio)
        inventario.append(producto)
        print('Producto agregado exitosamente.')
    except ValueError:
        print('Entrada inválida. Asegúrate de ingresar un número válido para cantidad y precio.')
    except Exception as e:
        print(f'Error al agregar el producto: {e}')
    input("\nPresiona Enter para continuar...")

def mostrar_inventario(inventario):
    if not inventario:
        print('No hay productos en el inventario.')
    else:
        for producto in inventario:
            print(producto)
            print('-' * 20)
    input("\nPresiona Enter para continuar...")

def buscar_producto(inventario):
    try:
        nombre_buscar = input('Introduce el nombre del producto a buscar: ').lower().strip()
        encontrado = next((producto for producto in inventario if producto.nombre.lower() == nombre_buscar), None)
        if encontrado:
            print(encontrado)
        else:
            print('Producto no encontrado.')
    except Exception as e:
        print(f'Error al buscar el producto: {e}')
    input("\nPresiona Enter para continuar...")

def actualizar_producto(inventario):
    try:
        nombre_actualizar = input('Introduce el nombre del producto a actualizar: ').lower().strip()
        for producto in inventario:
            if producto.nombre.lower() == nombre_actualizar:
                producto.cantidad = int(input('Introduce la nueva cantidad: '))
                producto.precio = float(input('Introduce el nuevo precio: '))
                print('Producto actualizado.')
                return
        print('Producto no encontrado.')
    except ValueError:
        print('Entrada inválida. Asegúrate de ingresar un número válido para cantidad y precio.')
    except Exception as e:
        print(f'Error al actualizar el producto: {e}')
    input("\nPresiona Enter para continuar...")

def eliminar_producto(inventario):
    try:
        nombre_eliminar = input('Introduce el nombre del producto a eliminar: ').lower().strip()
        inventario[:] = [producto for producto in inventario if producto.nombre.lower() != nombre_eliminar]
        print('Producto eliminado.') if any(producto.nombre.lower() == nombre_eliminar for producto in inventario) else print('Producto no encontrado.')
    except Exception as e:
        print(f'Error al eliminar el producto: {e}')
    input("\nPresiona Enter para continuar...")

def menu_inventario():
    inventario = []
    opciones = {
        1: agregar_producto,
        2: mostrar_inventario,
        3: buscar_producto,
        4: actualizar_producto,
        5: eliminar_producto
    }
    while True:
        limpiar_pantalla()
        print('\nSistema de Inventarios JR')
        print('1. Agregar producto')
        print('2. Mostrar todos los productos')
        print('3. Buscar producto por nombre')
        print('4. Actualizar producto')
        print('5. Eliminar producto por nombre')
        print('6. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion](inventario)
            elif opcion == 6:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')
            input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    menu_inventario()

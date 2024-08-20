import os

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "No se puede dividir entre cero."

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_calculadora():
    calc = Calculadora()
    while True:
        limpiar_pantalla()
        print('\nCalculadora')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion in [1, 2, 3, 4]:
                a = float(input('Introduce el primer número: '))
                b = float(input('Introduce el segundo número: '))
                if opcion == 1:
                    print(f'Resultado: {calc.sumar(a, b)}')
                elif opcion == 2:
                    print(f'Resultado: {calc.restar(a, b)}')
                elif opcion == 3:
                    print(f'Resultado: {calc.multiplicar(a, b)}')
                elif opcion == 4:
                    print(f'Resultado: {calc.dividir(a, b)}')
            elif opcion == 5:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')
        input("\nPresiona Enter para continuar...")

if __name__ == '__main__':
    menu_calculadora()

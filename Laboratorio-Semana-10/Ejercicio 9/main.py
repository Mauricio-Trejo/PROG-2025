'''
IMPLEMENTACIÓN DE MÚLTIPLES PARADIGMAS

Desarrolla un programa que implemente diferentes paradigmas
de programación:
* Imperativa: uso de estructuras de control como condicionales y bucles.
* Estructurada: separar código en funciones bien definidas.
* Modular: Crear diferentes módulos para funcionalidades específicas.
* Orientada a objetos: definir clases y objetos.

El programa debe mostrar el uso de cada paradigma con ejemplos claros.
'''

import interfaz, vehiculos

def ejecutar_programa():
    while True:
        interfaz.menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        interfaz.ejecutar_opcion(opcion)
        if opcion == 5:
            break

if __name__ == "__main__":
    # Inicializamos el sistema de vehículos
    vehiculos.sistema = vehiculos.SistemaVehiculos()
    
    # Ejecutamos el programa
    ejecutar_programa()

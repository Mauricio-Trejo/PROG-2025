'''
MÓDULO PARA CONVERSIÓN DE UNIDADES

Crea un módulo de Python llamado conversor.py que contenga funciones para
convertir:
* Kilometros a millas.
* Celsius a Fahrenheit.
* Litros a galones.

Luego, crea un programa principal que importe el módulo y permita al usuario
realizar conversiones.

'''

menu = '''
#   MENÚ
#
#   1. Kilometros a millas
#   2. Celsius a Fahrenheit
#   3. Litros a galones
#   4. Salir
#
'''
# Importamos módulo
import conversor

while True:
    print(menu)
    opt = input('Ingrese una opción (1/2/3/4): ')
    if opt == '1':
        kilometros = float(input('Ingrese la distancia en kilómetros: '))
        resultado = conversor.distancia(kilometros) # Se calcula por el módulo la conversión
        print(f'{kilometros:.3f} kilometros → {resultado:.3f} millas')
        input('Presione una tecla para continuar...')
    elif opt == '2':
        centigrados = float(input('Ingrese los grados centigrados: '))
        resultado = conversor.temperatura(centigrados) # Se calcula por el módulo la conversión
        print(f'{centigrados}° celsius → {resultado:.3f}° fahrenheit')
        input('Presione una tecla para continuar...')
    elif opt == '3':
        litros = float(input('Ingrese los litros: '))
        resultado = conversor.volumen(litros)
        print(f'{litros} litros → {resultado:.3f} galones') # Se calcula por el módulo la conversión
        input('Presione una tecla para continuar...')
    elif opt == '4':
        break
    else:
        print('Error: opción inválida.')
        input('Presione una tecla para continuar...')
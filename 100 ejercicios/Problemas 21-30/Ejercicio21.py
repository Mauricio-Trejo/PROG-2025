# Calcular el área y volumen de distintas figuras geometricas

menuA = '''
#
#   Menú de áreas
#
#   1. Cuadrado
#   2. Rectángulo
#   3. Triángulo
#   4. Círculo
#   5. Trapecio
#   6. Rombo
#   7. Volver
#
'''

menuV = '''
#
#   Menú de volúmenes
#
#   1. Cubos
#   2. Prisma rectangular
#   3. Piramide (base cuadrada o rectangular)
#   4. Cono
#   5. Esfera
#   6. Cilindro
#   7. Volver
#
'''

def areaCuadrado():
    lado = float(input('Ingrese la longitud de uno de los lados del cuadrado: '))
    return lado ** 2

def areaRectangulo():
    base = float(input('Ingrese la longitud de la base: '))
    altura = float(input('Ingrese la altura: '))
    return base * altura

def areaTriangulo():
    base = float(input('Ingrese la longitud de la base: '))
    altura = float(input('Ingrese la altura: '))
    return base * altura / 2

def areaCirculo():
    radio = float(input('Ingrese la longitud del radio: '))
    return math.pi * radio ** 2

def areaTrapecio():
    baseM = float(input('Ingrese la longitud de la base mayor: '))
    basem = float(input('Ingrese la longitud de la base menor: '))
    altura = float(input('Ingrese la altura: '))
    return (baseM + basem) * altura / 2

def areaRombo():
    dMayor = float(input('Ingrese la longitud de la diagonal mayor: '))
    dMenor = float(input('Ingrese la longitud de la diagonal menor: '))
    return dMayor * dMenor / 2

def volumenCubo():
    lado = float(input('Ingrese la longitud de uno de sus lados: '))
    return lado ** 3

def volumenPrismaR():
    ancho = float(input('Ingrese el ancho del prisma: '))
    largo = float(input('Ingrese el largo del prisma: '))
    altura = float(input('Ingrese la altura: '))
    return largo * ancho * altura

def volumenPiramide():
    base = float(input('Ingrese el área de la base: '))
    altura = float(input('Ingrese la altura: '))
    return base * altura / 3

def volumenCono():
    radio = float(input('Ingresa la longitud del radio: '))
    altura = float(input('Ingrese la altura: '))
    return altura * math.pi * radio ** 2 / 3

def volumenEsfera():
    radio = float(input('Ingresa la longitud del radio: '))
    return 4 / 3 * math.pi * radio ** 3

def volumenCilindro():
    radio = float(input('Ingresa la longitud del radio: '))
    altura = float(input('Ingrese la altura: '))
    return altura * math.pi * radio ** 2

import math

bMenuA = True
bMenuV = True
bandera = True

while bandera:
    op = input('¿Deseas calcular Área o Volumen? (A / V)\nPresiona X para salir.\n-> ').upper()
    if op == 'A':
        while bMenuA:
            print(menuA)
            op1 = int(input('Ingrese la opción deseada: '))
            if op1 == 1:
                print(areaCuadrado())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 2:
                print(areaRectangulo())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 3:
                print(areaTriangulo())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 4:
                print(areaCirculo())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 5:
                print(areaTrapecio())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 6:
                print(areaRombo())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 7:
                bMenuA = False
            else:
                print('Opción inválida.')
    elif op == 'V':
        while bMenuV:
            print(menuV)
            op1 = int(input('Ingrese la opción deseada: '))
            if op1 == 1:
                print(volumenCubo())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 2:
                print(volumenPrismaR())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 3:
                print(volumenPiramide())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 4:
                print(volumenCono())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 5:
                print(volumenEsfera())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 6:
                print(volumenCilindro())
                tskip = input('Presione una tecla para continuar...')
            elif op1 == 7:
                bMenuV = False
            else:
                print('Opción inválida.')
    elif op == 'X':
        bandera = False
    else:
        print('Opción inválida.')






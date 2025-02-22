# Simular el lanzamiento de un dado y una moneda

# Lanzamiento de una moneda

# Método 1
'''
import numpy as np
import scipy.stats as stats

p = 0.5  # probabilidad de cada caso

lanzamiento = stats.bernoulli.rvs(p)

print('Cara' if lanzamiento == 1 else 'Cruz')
'''

# Método 2

menu = '''
#   ELIGE UNA OPCIÓN
#
#   1. Lanzamiento de una moneda
#   2. Lanzamiento de un dado
#   3. Salir
#
'''
menuMoneda = '''
#   MONEDA
#
#   1. Volver a lanzar
#   2. Salir
#
'''

menuDado = '''
#   DADO
#
#   1. Volver a lanzar
#   2. Salir
#
'''

import random

contadorMoneda = 0
contadorDado = 0

def lanzamientoMoneda():
    global contadorMoneda
    opciones = ['Cara', 'Cruz']
    contadorMoneda += 1
    lanzamiento = random.choice(opciones)
    print(f'Lanzamiento {contadorMoneda}: ', lanzamiento)

def lanzamientoDado():
    global contadorDado
    contadorDado += 1
    lanzamiento = random.randint(1, 6)
    print(f'Lanzamiento {contadorDado}: ', lanzamiento)
    

bmenu = True

while bmenu:
    print(menu)
    op = input('--> ')
    if op == '1':
        lanzamientoMoneda()
        input('Presione una tecla para continuar...')
        bMoneda = True
        while bMoneda:
            print(menuMoneda)
            op2 = input('Elige una opción: ')
            if op2 == '1':
                lanzamientoMoneda()
                input('Presione una tecla para continuar...')
            elif op2 == '2':
                bMoneda = False
            else:
                print('Opción inválida.')  
    elif op == '2':
        lanzamientoDado()
        input('Presione una tecla para continuar...')
        bDado = True
        while bDado:
            print(menuDado)
            op2 = input('Elige una opción: ')
            if op2 == '1':
                lanzamientoDado()
                input('Presione una tecla para continuar...')
            elif op2 == '2':
                bDado = False
            else:
                print('Opción inválida.')
    elif op == '3':
        bmenu = False
    else:
        print('Opción inválida.')
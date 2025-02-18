#Crear una calculadora simple que realice operaciones básicas

'''
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

#Suma
suma = num1 + num2
#Resta
resta = num1 - num2
#Multiplicación
multi = num1 * num2

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multi)

try:
    divi = num1 / num2
    print("La división es: ", divi)
except ZeroDivisionError:
    print("No se puede dividir entre cero...")
'''

menu = """
#   Menú Principal
#
#   E -> Exponentes
#   M -> Multiplicaciones escalares
#   D -> División
#   A -> Adición
#   S -> Sustracción
#   X -> Salir
#
"""

bMenu1 = True

menu2 = """
#   Menú división
#
#   1 -> División
#   2 -> División Entera
#   3 -> División Residuo
#   4 -> Regresar a menú principal
#
"""
bMenu2 = True
bDiv0 = True
def exponentes(base, potencia):
    return base ** potencia

def multiplicacion(factor1, factor2):
    return factor1 * factor2

def division(dividendo, divisor):
    if divisor != 0:
        return dividendo/divisor
    else:
        while bDiv0:
            ndivisor = int(input("La división entre 0 es imposible todadvía.\nIngrese otro valor para el divisor"))
            if ndivisor != 0:
                bDiv0 = False
        return dividendo/division
    
def divisionEntera(dividendo, divisor):
    if divisor != 0:
        return dividendo//divisor
    else:
        while bDiv0:
            ndivisor = int(input("La división entre 0 es imposible todadvía.\nIngrese otro valor para el divisor"))
            if ndivisor != 0:
                bDiv0 = False
        return dividendo//division
    
def divisionResiduo(dividendo, divisor):
    if divisor != 0:
        return dividendo % divisor
    else:
        while bDiv0:
            ndivisor = int(input("La división entre 0 es imposible todadvía.\nIngrese otro valor para el divisor"))
            if ndivisor != 0:
                bDiv0 = False
        return dividendo % division
    
def leerNumeros():
    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))
    return num1, num2

def divisionMenu():
    while bMenu2:
        print(menu2)
        op2 = int(input('Ingrese la opción deseada: '))
        if op2 == 1:
            t1 = leerNumeros()
            division(t1[0], t1[1])
        elif op2 == 2:
            t2 = leerNumeros()
            divisionEntera(t2[0], t2[1])
        elif op2 == 3:
            t3 = leerNumeros()
            leerNumeros(t3[0], t3[1])
        else:
            print('Opción inválida')

def adicion(num1, num2):
    return num1 + num2

def sustraccion(num1, num2):
    return num1 - num2

while(bMenu1):
    print(menu)
    op = input('Ingrese la opción deseada: ').upper()
    if op == 'E':
        tE = leerNumeros()
        print(exponentes(tE[0], tE[1]))
    elif op == 'M':
        tM = leerNumeros()
        print(multiplicacion(tM[0], tM[1]))
    elif op == 'D':
        bMenu2 = True
        print(divisionMenu())
    elif op == 'A':
        tA = leerNumeros()
        print(adicion(tA[0], tA[1]))
    elif op == 'S':
        tS = leerNumeros()
        print(sustraccion(tS[0], tS[1]))

    elif op == 'X':
        bMenu1 = False
    else:
        print('Opción inválida')
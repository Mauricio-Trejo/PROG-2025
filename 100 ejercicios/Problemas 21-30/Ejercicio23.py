# Implementar y operar con matrices.

menu = '''
#   MENÚ
#
#   1. Suma de dos matrices
#   2. Multiplicación de matriz por escalar
#   3. Multiplicación de dos matrices
#   4. Traspuesta de una matriz
#   5. Salir
#
'''

def traspuesta_matriz():
    matriz, fila = list(), list()
    print('Ingrese la Matriz A: ')
    A = leerMatriz()
    if A != False:
        for i in range(len(A[0])):
            fila = []
            for j in range(len(A)):
                fila.append(A[j][i])
            matriz.append(fila)
        print('La matriz traspuesta es: ')
        imprimir_matriz(matriz)
    else:
        mensaje = 'Error al leer la matriz.'
        mensaje_error(mensaje)

def multiplicacion_matriz():
    elemento = 0
    matriz, fila = list(), list()
    print('Ingrese la Matriz A: ')
    A = leerMatriz()
    print('Ingrese la matriz B: ')
    B = leerMatriz()
    if A != False and B != False and len(A[0]) == len(B):
        print('A * B = ')
        for k in range(len(B[0])):
            fila = []
            for i in range(len(A)):
                for j in range(len(A[0])):
                    elemento += A[k][j]*B[j][i]
                fila.append(elemento)
                elemento = 0
            matriz.append(fila)
        imprimir_matriz(matriz)
    elif A == False or B == False:
        mensaje = 'Error al leer las matrices'
        mensaje_error(mensaje)
    else:
        mensaje = 'Error: las matrices no son multiplicables.'
        mensaje_error(mensaje)

def multiplicacion_escalar():
    matriz = list()
    escalar = float(input('Ingresa el escalar: '))
    print('Ingrese la matriz A: ')
    A = leerMatriz()
    if A != False:
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] * escalar)
            matriz.append(fila)
        imprimir_matriz(matriz)
    else:
        mensaje = 'Error al leer la matriz'
        mensaje_error(mensaje)

def suma():
    print('Ingrese la matriz A: ')
    A = leerMatriz()
    print('Ingrese la matriz B: ')
    B = leerMatriz()
    matriz = list()
    fila = list()
    if A != False and B != False and len(A) == len(B) and len(A[0]) == len(B[0]) :
        for i in range(len(A)):
            fila = [] # Aquí se 'limpia' la lista por una vacía
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            matriz.append(fila)
        imprimir_matriz(matriz)
    elif A == False or B == False:
        mensaje = 'Error al leer la matriz.'
        mensaje_error(mensaje)
    else:
        mensaje = 'Error: las matrices no son sumables.'
        mensaje_error(mensaje)

def leerMatriz():
    matriz = list()
    try:
        m = int(input('Ingresa el número de filas: '))
        n = int(input('Ingresa el número de columnas: '))
        for i in range(m):
            validacion = True
            while validacion:
                numeros = input(f'Ingresa los números de la fila {i+1} separados por espacios.\n--> ')
                filas = list(map(int, numeros.split()))
                if len(filas) != n:
                    print('Error: el número de elementos no coincide con el número de columnas.\nVuelve a intentarlo.')
                else:
                    matriz.append(filas)
                    validacion = False
        return matriz
    except ValueError:
        print('Error: los elementos a ingresar tienen que ser números.')          
        return False

def mensaje_error(mensaje):
    print(mensaje)

def imprimir_matriz(matriz):
    try:
        for fila in matriz:
                for elemento in fila:
                    print(elemento, end=" ")
                print() 
    except:
        return matriz


bmenu = True
while bmenu:
    print(menu)
    op = input('Ingrese una opción: ')
    if op == '1':
        suma()
        input('Presione una tecla para continuar...')
    elif op == '2':
        multiplicacion_escalar()
        input('Presione una tecla para continuar...')
    elif op == '3':
        multiplicacion_matriz()
        input('Presione una tecla para continuar...')
    elif op == '4':
        traspuesta_matriz()
        input('Presione una tecla para continuar...')
    elif op == '5':
        bmenu = False
    else:
        print('Opción Inválida.')
        input('Presione una tecla para continuar...')
        
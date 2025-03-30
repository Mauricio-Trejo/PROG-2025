'''
MANEJO DE INVENTARIO CON LISTAS Y DICCIONARIOS

Implementa un sistema de inventario con las siguientes funcionalidades:
* Permitir al usuario agregar productos, especificando nombre, categoría,
precio y cantidad.
* Permitir la eliminación de productos por su nombre.
* Buscar productos por nombre y mostrar su información.
* Mostrar todos los productos ordenados por precio de mayor a menor.
'''
bd = list() #Creamos una lista vacía para la base de datos

def agregar():
    nombre = input('Ingresa el nombre del producto: ').lower() # Convertimos a minúsculas por conveniencia
    categoria = input('Ingresa la categoría del producto: ').lower()
    precio = input('Ingresa el precio del producto: ')
    cantidad = input('Ingresa la cantidad de productos: ')
    producto_existe = any( elemento['nombre'] == nombre for elemento in bd) # any() devuelve True si la condición se cumple (si el producto ya existe)
    
    if producto_existe:
        print('Error: el producto que ingresaste ya existe en los registros.')
    else:
        registro = {'nombre': nombre, 'categoria': categoria, 'precio': precio, 'cantidad': cantidad} # Creamos el diccionario (registro)
        bd.append(registro) # Se agrega a la base de datos
        print('El producto ha sido registrado correctamente.')

def eliminar():
    global bd
    nombre = input('Ingresa el nombre del producto que deseas eliminar: ').lower()
    producto_existe = any(elemento['nombre'] == nombre for elemento in bd) # Verifica si existe el registro
    if producto_existe:
        bd = [elemento for elemento in bd if elemento['nombre'] != nombre] # Se reescribe la variable bd con los elemenos modificados
        print('El producto ha sido eliminado de los registros correctamente.')
    else:
        print('Error: el producto no se encuentra en los registros.')

def buscar():
    global bd
    nombre = input('Ingresa el nombre del producto a buscar: ').lower()
    producto_existe = any(elemento['nombre'] == nombre for elemento in bd) # Verifica si existe el registro
    if producto_existe:
        for elemento in bd:
            if elemento['nombre'] == nombre: # Se busca el registro por el nombre
                print(f"Nombre: {elemento['nombre']}")
                print(f"Categoría: {elemento['categoria']}")
                print(f"Precio: ${elemento['precio']}")
                print(f"Cantidad: {elemento['cantidad']}")
                break
    else:
        print('Error: el producto no se encuentra en los registros.')

def consulta():
    global bd
    if len(bd) > 0: # Verifica si la base da datos tiene elementos
        for elemento in bd:
            print(f"Nombre: {elemento['nombre']}")
            print(f"Categoría: {elemento['categoria']}")
            print(f"Precio: ${elemento['precio']}")
            print(f"Cantidad: {elemento['cantidad']}")
            print()
    else:
        print('No se ha registrado nada aún.')
    
    


menu = '''
#   MENÚ
#
#   1. Agregar productos
#   2. Eliminar productos
#   3. Buscar productos
#   4. Mostrar todos los productos
#   5. Salir
'''

while True:
    print(menu)
    opt = input('Ingrese una opción (1/2/3/4/5): ')
    if opt == '1':
        agregar()
        input('Presione una tecla para continuar...')
    elif opt == '2':
        eliminar()
        input('Presione una tecla para continuar...')
    elif opt == '3':
        buscar()
        input('Presione una tecla para continuar...')
    elif opt == '4':
        consulta()
        input('Presione una tecla para continuar...')
    elif opt == '5':
        break
    else:
        print('Error: ingresa una opción válida')
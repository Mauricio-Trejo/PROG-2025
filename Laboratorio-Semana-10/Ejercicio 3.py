'''
GESTIÓN DE CONTACTOS CON TUPLAS Y ESTRUCTURAS ANIDADAS

Desarrolla un programa que permita gestionar contactos de la siguiente manera:
* Cada contacto debe ser almacenado como una tupla con nombre, número y correo.
* La agenda de contactos debe almacenarse en una lista.
* Debe permitir agregar nuevos contactos.
* Buscar contactos por nombre e imprimir sus detalles.
* Listar todos los contactos en orden alfabético.

'''

agenda = list()
contacto = tuple()

def agregar():
    nombre = input('Ingrese el nombre: ')
    numero = input('Ingrese el número: ')
    correo = input('Ingrese el correo: ')
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print('El contacto se ha registrado correctamente.')

def buscar():
    if len(agenda) > 0: #Verifica si la lista está vacía o no
        bandera = False
        nombre = input('Ingrese el nombre del contacto a buscar: ')
        for contactos in agenda:
            if contactos[0] == nombre: # Puede haber 1 ó más contactos con el mismo nombre
                bandera = True
                print(f'Nombre: {contactos[0]}')
                print(f'Número: {contactos[1]}')
                print(f'Correo: {contactos[2]}')
        if not bandera:
            print('Error: no se encontró ningún contacto')
    else:
        print('No se han registrado contactos a la agenda.')
    
def consulta():
    if len(agenda) > 0: # Verifica si la lista está vacía o no
        print('LISTA DE CONTACTOS (A-Z)')
        agenda.sort() # Ordena la lista de mayor a menor
        for contacto in agenda:
            print(f'* {contacto[0]}')
    else:
        print('No se han agregado contactos a la agenda.')

menu = '''
#   MENÚ
#   
#   1. Agregar contactos
#   2. Buscar contactos
#   3. Lista de contactos
#   4. Salir
#
'''

while True:
    print(menu)
    opt = input('Ingresa una opción (1/2/3/4): ')
    if opt == '1':
        agregar()
        input('Presione una tecla para continuar...')
    elif opt == '2':
        buscar()
        input('Presione una tecla para continuar...')
    elif opt == '3':
        consulta()
        input('Presione una tecla para continuar...')
    elif opt == '4':
        break
    else:
        print('Error: opción inválida')
        input('Presione una tecla para continuar...')
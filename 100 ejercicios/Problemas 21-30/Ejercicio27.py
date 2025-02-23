#   Crear un conversor de unidades

menu = '''
#   CONVERSOR DE UNIDADES
#
#   1. Metros ↔ Kilometros
#   2. Gramos ↔ Kilogramos
#   3. Centimetros ↔ Metros
#   4. Gramos ↔ miligramos
#   5. Salir
#
'''

conversiones = dict()

conversiones = {
    'metros': {'kilometros': 0.001, 'centimetros': 100, 'milimetros': 1000},
    'kilogramos': {'gramos': 1000, 'miligramos': 1000000},
    'centimetros': {'metros': 0.01, 'milimetros': 10},
    'gramos': {'kilogramos': 0.001, 'miligramos': 1000}
}

def conversion(valor, de_unidades, a_unidades):
    if de_unidades not in conversiones or a_unidades not in conversiones[de_unidades]:
        return "Conversión no disponible"
    else:
        factor = conversiones[de_unidades][a_unidades]

    return valor * factor

bmenu = True
while bmenu:
    print(menu)
    op = input('Ingrese una opción: ')
    if op == '1':
        valor = float(input('Ingrese el valor: '))
        de_unidades = input('De qué unidad (metros o kilometros): ').lower()
        a_unidades = input('A qué unidad (metros o kilometros): ').lower()
        resultado = conversion(valor, de_unidades, a_unidades)
        print(f'{valor} {de_unidades} es igual a {resultado} {a_unidades}')
        input('Presione una tecla para continuar...')
    elif op == '2':
        valor = float(input('Ingrese el valor: '))
        de_unidades = input('De qué unidad (gramos o kilogramos): ').lower()
        a_unidades = input('A qué unidad (gramos o kilogramos): ').lower()
        resultado = conversion(valor, de_unidades, a_unidades)
        print(f'{valor} {de_unidades} es igual a {resultado} {a_unidades}')
        input('Presione una tecla para continuar...')
    elif op == '3':
        valor = float(input('Ingrese el valor: '))
        de_unidades = input('De qué unidad (centimetros o metros): ').lower()
        a_unidades = input('A qué unidad (centimetros o metros): ').lower()
        resultado = conversion(valor, de_unidades, a_unidades)
        print(f'{valor} {de_unidades} es igual a {resultado} {a_unidades}')
        input('Presione una tecla para continuar...')
    elif op == '4':
        valor = float(input('Ingrese el valor: '))
        de_unidades = input('De qué unidad (gramos o miligramos): ').lower()
        a_unidades = input('A qué unidad (gramos o miligramos): ').lower()
        resultado = conversion(valor, de_unidades, a_unidades)
        print(f'{valor} {de_unidades} es igual a {resultado} {a_unidades}')
        input('Presione una tecla para continuar...')
    elif op == '5':
        bmenu = False
    else:
        print('Opción inválida. Vuelve a intentarlo.')

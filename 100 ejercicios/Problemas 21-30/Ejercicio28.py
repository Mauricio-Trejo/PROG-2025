# Simular una cuenta bancaria con depósitos y retiros
menu = '''
#   MENU
#
#   1. Ver saldo
#   2. Depositar
#   3. Retirar
#   4. Salir
#
'''
def mostrar_saldo(saldo):
    print(f"Saldo actual: ${saldo:.2f}")

def deposito(saldo, cantidad):
    if cantidad > 0:
        saldo += cantidad
        print(f"Depósito exitoso de ${cantidad:.2f}.")
    else:
        print("La cantidad a depositar debe ser mayor a 0.")
    return saldo

def retiro(saldo, cantidad):
    if cantidad > 0:
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad:.2f}.")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    else:
        print("La cantidad a retirar debe ser mayor a 0.")
    return saldo


saldo = 0
bmenu = True
while bmenu:
    print(menu)
    opcion = input('Elige una opción: ')
    
    if opcion == "1":
        mostrar_saldo(saldo)
        input('Presione una tecla para continuar...')
    elif opcion == "2":
        cantidad = float(input("¿Cuánto deseas depositar? $"))
        saldo = deposito(saldo, cantidad)
        input('Presione una tecla para continuar...')
    elif opcion == "3":
        cantidad = float(input("¿Cuánto deseas retirar? $"))
        saldo = retiro(saldo, cantidad)
        input('Presione una tecla para continuar...')
    elif opcion == "4":
        bmenu = False
    else:
        print("Opción inválida. Intenta de nuevo.")
        input('Presione una tecla para continuar...')
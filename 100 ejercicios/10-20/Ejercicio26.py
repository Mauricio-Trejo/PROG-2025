# Implementar una agenda de contactos

bandera = True
contador = 1
listaContactos = list()

while bandera:
    op = input(f"Cantidad de contactos: {contador-1} \n¿Desea agregar un contacto?(S/N): ")
    if op.lower() == 's':
        contacto = dict()
        contacto['identificador'] = input(f'Ingrese el identificador de contacto {contador}: ')
        contacto['numero'] = input(f'Ingrese número de contacto {contador}: ')
        contador += 1
        listaContactos.append(contacto)
    else:
        break 

print(listaContactos)





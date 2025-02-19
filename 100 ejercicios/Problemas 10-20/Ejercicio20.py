# Implementar busqueda binaria y lineal
    
def busquedaLineal(lista, objetivo):
    for index, elemento in enumerate(lista):
        if objetivo == elemento:
            return index
    return print('NO se encontró el elemento')

def busquedaBinaria(lista, objetivo):
    inicio = 0
    fin = len(lista)-1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return print('NO se encontró el elemento')

lim = int(input('¿Cuántos números deseas ingresar a la lista? -> '))
lista = list()
bandera = True
for x in range(lim):
    num = float(input(f'Ingresa el {x+1}° número: '))
    lista.append(num)

listaOrdenada = sorted(lista) # sorted() devuelve una lista ordenada

# Para ordenar una lista se puede usar lista.sort()

objetivo = float(input('Ingresa el objetivo a buscar: '))

print(lista)
print(listaOrdenada)

print(f'Busqueda Binaria.\nEl objetivo ({objetivo}) se encuentra en la posición {busquedaBinaria(listaOrdenada, objetivo)}')
print(f'Busqueda Lineal.\nEl objetivo ({objetivo}) se encuentra en la posición {busquedaLineal(lista, objetivo)} ')


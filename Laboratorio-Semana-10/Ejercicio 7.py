'''
ORDENAMIENTO Y BÚSQUEDA

Implementa un programa que realice lo siguiente:
* Genere una lista de número aleatorios.
* Ordene la lista usando el algoritmo de Quicksort
* Permita al usuario buscar un número en la lista usando busqueda binaria.

El programa debe mostrar la lista antes y después del ordenamiento y los
resultados de la búsqueda.

'''

def quicksort(lista):
    if len(lista) <= 1:
        return lista # La lista solo tiene 1 ó 0 elementos ("ya está ordenada").
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote] # Si son menores o igual a la referencia
        mayores = [x for x in lista[1:] if x > pivote] # Si son mayores a la referencia
        return quicksort(menores) + [pivote] + quicksort(mayores)

def busqueda_binaria(lista, num_buscado):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if num_buscado == lista[medio]:
            return medio
        elif lista[medio] > num_buscado:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1


import random

n = int(input('Ingresa la cantidad de números que quieres en la lista: '))

lista = [random.randint(0, 100) for _ in range(n)]

lista_ordenada = quicksort(lista)

print(lista)
print(lista_ordenada)

num = int(input('Ingresa el número de la lista a buscar: '))
numero = busqueda_binaria(lista_ordenada, num)
if numero != -1:
    print(f'El número {num} se encuentra en el índice {numero}')
else:
    print(f'El número {num} no está en la lista')
'''
IMPLEMENTACIÓN DE MERGESORT

Implementa el algoritmo de Mergesort para ordenar una lista de números
ingresada por el usuario. El programa debe mostrar la lista antes y
después del ordenamiento.

'''

def mergesort(lista):
    if len(lista) > 1:
        # dividimos la lista en dos mitades
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        # Aplicamos recursividad
        mergesort(izquierda)
        mergesort(derecha)

        i = k = j = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

numeros = input('Ingresa una lista de números separados por un espacio: ')

lista = list(map(int, numeros.split()))
print(lista)
mergesort(lista)
print(lista)
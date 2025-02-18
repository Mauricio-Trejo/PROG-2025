# Implementar estructura de datos básica: pila, cola y lista enlazada.

#Pila, Cola, lista enlazada

#pila = list()

# Para pila
def insertarPila(pila, elemento):
    pila.append(elemento)
    return pila

def eliminarPila(pila):
    elementoFinal = pila[len(pila)-1]
    pila.remove(elementoFinal)
    return pila


if __name__ == "__main__":
    estupila = list()
    insertarPila(estupila,1)
    print(estupila)
    insertarPila(estupila,"mi pelo")
    print(estupila)
    insertarPila(estupila,"ideota")
    print(estupila)
    eliminarPila(estupila)
    print(estupila)

# Para cola
def insertarCola(cola, elemento):
    cola.append(elemento)
    return cola

def eliminarCola(cola):
    firstItem = cola[0]
    cola.remove(firstItem)
    return cola

contenedor = list()

insertarCola(contenedor, 12)
print(contenedor)
insertarCola(contenedor, 'Que onda')
print(contenedor)
insertarCola(contenedor, 'MUNDO')
print(contenedor)
eliminarCola(contenedor)
print(contenedor)
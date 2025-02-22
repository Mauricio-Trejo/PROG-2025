# Calcular la suma de una serie numérica

def suma_serie():

    try:
        numeros = input('Ingrese una serie de números separados por espacios: ')

        lista_numeros = list(map(float, numeros.split()))
        # numeros.split() devuelve un iterable de los números pedidos separados por los espacios
        # map(function, iterable) aplica la función a cada elemento del iterable, devuelve un iterable sin guardarlo en la memoria
        #list() castea el iterable (sin guardar) y genera un interable (lista) y lo guarda en la memoria

        suma = sum(lista_numeros)
        print(f'La suma de la series es: {suma}')

    except:
        print('Error: asegurese de ingresar solo números separados por espacios.')

suma_serie()
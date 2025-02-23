# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Función recursiva para calcular el n-ésimo número de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Función recursiva para calcular la suma de los elementos de una lista
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Prueba de las funciones
print("Factorial de 5:", factorial(5))  # Resultado esperado: 120
print("Fibonacci de 6:", fibonacci(6))  # Resultado esperado: 8
print("Suma de la lista [1, 2, 3, 4, 5]:", suma_lista([1, 2, 3, 4, 5]))  # Resultado esperado: 15

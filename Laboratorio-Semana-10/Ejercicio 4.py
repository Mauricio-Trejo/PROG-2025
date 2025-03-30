'''
CALCULADORA DE ESTADÍSTICAS

Crea una función que reciba una lista de números y devuelva:
* Promedio, mediana y desviación estándar.
* Debe permitir un número arbitrario de argumenos usando *args.
* Utilizar funciones lambda para cálculos simples como la media.

El programa debe solicitar al usuario una lista de números y mostrar los resultados

'''

import math

# Función para calcular el promedio, mediana y desviación estándar
def estadisticas(*args): # *args se comporta como una tupla
    # Promedio utilizando lambda
    promedio = lambda nums: sum(nums) / len(nums)
    
    # Mediana
    def mediana(nums):
        nums = sorted(nums)  # Ordenamos los números de menor a mayor
        n = len(nums)
        if n % 2 == 0:  # Si hay un número par de elementos
            return (nums[n // 2 - 1] + nums[n // 2]) / 2  # Promedio de los dos del medio
        else:  # Si hay un número impar de elementos
            return nums[n // 2]  # El elemento del medio
    
    # Desviación estándar
    def desviacion_estandar(nums):
        mean = promedio(nums)  # Usamos la función lambda para calcular el promedio
        varianza = sum((x - mean) ** 2 for x in nums) / len(nums)  # Varianza
        return math.sqrt(varianza)  # Raíz cuadrada de la varianza para obtener la desviación estándar
    
    # Calcular estadísticas
    promedio_valor = promedio(args)  # Calcula el promedio
    mediana_valor = mediana(args)  # Calcula la mediana
    desviacion_valor = desviacion_estandar(args)  # Calcula la desviación estándar
    
    return promedio_valor, mediana_valor, desviacion_valor

# Solicitar lista de números al usuario
entrada = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números (flotantes)
numeros = list(map(float, entrada.split())) # map aplica la función float a cada elemento del iterable

# Calcular estadísticas
promedio, mediana, desviacion = estadisticas(*numeros) # *numeros descompone la lista en números individuales

# Mostrar resultados
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")

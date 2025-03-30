# Análisis de texto con diccionarios y conjuntos

'''
Desarrolla un programa que analice un texto ingresado por
el usuario y determine:

* El número total de palabras en el texto.
* La cantidad de palabras únicas, utilizando un conjunto para evitar
repeticiones.
* La frecuencia de cada palabra usando un diccionario donde la clave
sea la palabra y el valor la cantidad de veces que aparece.
* La palabra más frecuente y cuántas veces aparece.

El programa debe mostrar un resumen con estos datos.
'''
def impresionDiccionario(dicc):
    return '\n'.join([f'{clave}: {valor}' for clave, valor in dicc.items()])

import string
# Aquí se abre el archivo de texto
with open('Laboratorio-Semana-10/texto.txt', 'r', encoding='utf-8') as handler:
    texto = handler.read()
    # Quitamos signos de puntuación con le uso de la librería 'string' importada anteriormente
    texto_depurado = texto.translate(str.maketrans('', '', string.punctuation))

    palabras = texto_depurado.lower().split()   # convertimos a minúsculas y creamos una lista
    pUnicas = set(palabras)    # Creamos el conjunto de palabras únicas
    contadorP = len(palabras)   # Cantidad de palabras totales (tamaño de la lista)
    contadorPU = len(pUnicas)   # Cantidad de palabras únicas (tamaño del conjunto)
    diccionario = dict()
    diccionario = {palabra: palabras.count(palabra) for palabra in pUnicas} # Creamos diccionario de palabras y su frecuencia
    lst = list(diccionario.items()) # Lista de tuplas de los elemenos del diccionario
    lst = [(valor, clave) for clave, valor in lst] # Cambio de orden de las tuplas de las listas
    lst.sort(reverse=True)  # Ordenar de mayor a menor la frecuencia de las palabras

resumen = f'''
Total de palabras: {contadorP}
Palabras únicas: {contadorPU}
Frecuencia de palabras: {impresionDiccionario(diccionario)}
Palabra más frecuente: "{lst[0][1]}"  Frecuencia: {lst[0][0]}
'''
print(resumen)
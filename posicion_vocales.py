#   PROBLEMA 2

'''
def ubicadorDeVocales(cadena):
    vocales = dict()
    cadenaN = cadena.lower()
    indices = list()
    indices = [[], [], [], [], []]
    for index in range(len(cadena)):
        if cadena[index] == 'a':
            indices[0].append(index)
        if cadena[index] == 'e':
            indices[1].append(index)
        if cadena[index] == 'i':
            indices[2].append(index)
        if cadena[index] == 'o':
            indices[3].append(index)
        if cadena[index] == 'u':
            indices[4].append(index)
    
    vocales['a'] = indices[0]
    vocales['e'] = indices[1]
    vocales['i'] = indices[2]
    vocales['o'] = indices[3]
    vocales['u'] = indices[4]

    return vocales

cadena = input('Ingresa una cadena de caracteres: ')
print(ubicadorDeVocales(cadena))
print(ubicadorDeVocales('murcielago'))
'''

def ubicadorDeVocales(cadena):
    elementos = 'aeiou'
    cadenaN = cadena.lower()
    vocales = {vocal: [] for vocal in elementos} #Inicializamos el diccionario

    for index, letra in enumerate(cadenaN): 
        #enumerate() devuelve un iterable con n tuplas (index, cadena[index])
        if letra in vocales:
            vocales[letra].append(index)

    return vocales

cadena = input('Ingrese una cadena de caraceres: ')
print(ubicadorDeVocales(cadena))
print(ubicadorDeVocales('murcielago'))
print(ubicadorDeVocales('Eucalipto'))
print(ubicadorDeVocales('Albericoque'))
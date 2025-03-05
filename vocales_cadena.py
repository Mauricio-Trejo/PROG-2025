#   PROBLEMA 1
'''
def contadorDeVocales(cadena):
    cadena_nueva = cadena.lower()
    vocales = dict()
    vocales['a'] = cadena_nueva.count('a')
    vocales['e'] = cadena_nueva.count('e')
    vocales['i'] = cadena_nueva.count('i')
    vocales['o'] = cadena_nueva.count('o')
    vocales['u'] = cadena_nueva.count('u')

    return vocales
'''
def contadorDeVocales(cadena):
    cadenaN = cadena.lower()
    vocales = {vocal: cadenaN.count(vocal) for vocal in 'aeiou'}

    return vocales


cadena = input('Ingresa una cadena de caracteres: ')

print(contadorDeVocales(cadena))
print(contadorDeVocales('murcielago'))
print(contadorDeVocales('eucalipto'))
print(contadorDeVocales('Albericoque'))

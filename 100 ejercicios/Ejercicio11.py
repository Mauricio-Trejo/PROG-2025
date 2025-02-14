# Verificar si una cadena es un palíndromo

palabra = input('Ingresa una palabra para verificar si es un palíndromo: ')
cadena = palabra.lower().replace(' ', '')
inverso = cadena[::-1]
if cadena == inverso:
    print('"%s" SI es un palíndromo.' %palabra)
    print(cadena, inverso)
else:
    print('"%s" NO es un palíndromo.' %palabra)
    print(cadena, inverso)
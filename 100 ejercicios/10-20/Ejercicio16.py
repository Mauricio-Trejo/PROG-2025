# Contar el número de vocales y consonantes en una cadena

cadena = input('Ingresa una palabra u oración: ')
control = cadena.lower().replace(' ', '')

vocales = 0
consonantes = 0

for x in range(len(control)):
    if 'a' == control[x] or 'e' == control[x] or 'i' == control[x] or 'o' == control[x] or 'u' == control[x]:
        vocales += 1
    else:
        consonantes += 1


print('"%s" tiene %d vocales y %d consonantes' % (cadena, vocales, consonantes))
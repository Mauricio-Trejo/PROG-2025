# Cadenas y sus métodos

cadena = str()
cadena = 'mundo'

print(type(cadena))
print(dir(cadena)) #función dir sirve para desglosar los métodos del objeto
help(str.capitalize) #función help sirve para describir el método
print(cadena.capitalize()) # retorna el valor 'capitalizado'

palabra = '     Hola mundo que tal      '
print(palabra.strip()) # strip() elimina los espacios en blanco, tabs o nuevas lineas al INICIO y FINAL de la sentencia

palabra2 = 'pizza'
help(str.count)
print(palabra2.count('a', 3, 5)) # count() cuenta cuantas aparece un caracter o subcadena en una cadena
#cadena.count(str, index start, index end)

# Formatear cadenas
print('En %d años yo he visto %g %s.'% (3, 0.1, 'camellos'))  
# %d formatea enteros, %g formatea flotantes, %s formatea cadenas
# Cuando hay dos o más % se tiene que crear una tupla con los datos a formatear dentro del print('%d cadena %g (tupla)')
print('Tengo %d años' % 18) 
#Cuando hay un solo % se agrega despues de las comillas print('%d cadena' % 18)



cad = 'X-DSPAM-Confidence:0.8475'
pos1 = cad.find(':')
num = float(cad[pos1+1:])
print(num, type(num))


cadenaNumeros = '45411511616'
print(cadenaNumeros.isnumeric()) # Verificar si toda la cadena hay caracteres numéricos, retorna True

grupo = 'mauricio'
print(grupo[::-1]) # palabra[desde i (empieza en cero) : hasta j : pasos]

#Tipos de variables

str()
int()
float()

#Tipos de datos estructurados
list()
dict()
set()
tuple()
#enumerate()
#range()

'''diasSemana = ['Lun', 'Mar', 'Mier', 'Jue', 'Vier']
print(diasSemana, type(diasSemana))
#Las listas pueden ser de datos combinados en Python

combinado= [1, 2.34, 'Alzhaimer', diasSemana]
print(combinado, type(combinado))

#Formas de declarar listas
lista = list([1,2,3])
lista = [[0,0,0]*4]*10
'''
lista = list()
#Conjuntos
conjunto = set()
#Cuando se define un conjunto de manera 'bulgar' tiene que haber elementos dentro de {} para diferenciarlo de un diccionario

from random import randint

for i in range(25):
    t = randint(90, 100)
    lista.append(t)
    conjunto.add(t)

print(lista)
print(conjunto)

#La diferencia de un conjunto y una lista es que el conjunto/set() solo almacena un número una sola vez sin repetir

tupla = tuple()
tupla = (3.14, 2.74, 1.62)

numerosLetra = {'pi': 3.14, 'e': 2.74, 'phi': 1.62}

print(numerosLetra['pi'])

numerosLetra['tau'] = 6.28

print(numerosLetra)
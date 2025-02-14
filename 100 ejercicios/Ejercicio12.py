# Encontrar el mayor entre tres números dados

# Método 1
'''a = int(input('Ingresa el 1° número: '))
b = int(input('Ingresa el 2° número: '))
c = int(input('Ingresa el 3° número: '))


if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c

print('El número mayor es: ', mayor)'''


# Método dos

'''
mayor = None    # None quiere decir 'vacío'
contador = 1
lista = list()
while contador <= 3:
    lista.append(int(input('Ingresa un número: ')))
    contador += 1

for valor in lista:
    print(valor, mayor)
    if mayor is None or valor > mayor:
        mayor = valor
        print(valor, mayor)

print('El número mayor es: ', mayor)
'''

# Método tres
contador = 1
lista = list()
while contador <= 3:
    lista.append(int(input('Ingresa un número: ')))
    contador += 1

mayor = max(lista)
print('El valor mayor es: ', mayor)




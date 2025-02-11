# Encontrar el mayor entre tres números dados

a = int(input('Ingresa el 1° número: '))
b = int(input('Ingresa el 2° número: '))
c = int(input('Ingresa el 3° número: '))

if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c

print('El número mayor es: ', mayor)
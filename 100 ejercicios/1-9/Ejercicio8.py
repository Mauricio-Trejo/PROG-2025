#Calcular el área y circunferencia de un circulo

radio = int(input('Ingresa la magnitud del radio del círculo: '))

import math
x = math.pi

area = x*radio**2
perimetro = 2*radio*x

print('El área del círculo es: ', area)
print('El perímetro del círculo es: ', perimetro)
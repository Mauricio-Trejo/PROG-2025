# Resolver ecuaciones cuadráticas

import math

print('Ecuación cuadrática de la forma ax² + bx + c = 0')
a = float(input('Ingresa el valor de a: '))
b = float(input('Ingresa el valor de b: '))
c = float(input('Ingresa el valor de c: '))
discriminante = (b**2)-(4*a*c)

try:
    x1 = ((-1*b) + (math.sqrt(discriminante))) / (2*a)
    x2 = ((-1*b) - (math.sqrt(discriminante))) / (2 * a)
    print('1° resultado: X = %g' % x1)
    print('2° resultado: X = %g' % x2)
except:
    print('El valor del discriminante es negativo %g, por lo que no existen valores reales' % discriminante)



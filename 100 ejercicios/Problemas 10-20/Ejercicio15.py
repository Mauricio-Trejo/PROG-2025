# Determinar si un año es bisiesto

''' Un año solo es bisiesto si:
1. Es divisible entre 4
2. Si es divisible entre 100 y entre 400

Si es divisible entre 4 y entre 100 pero no entre 400, NO es bisiesto
'''


num = int(input('Ingresa un año para determinar si es bisiesto: '))

if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print(num, ' es un año bisiesto')
        else:
            print(num, ' no es un año bisiesto')
    else:
        print(num, ' es año bisiesto')
else:
    print(num, ' no es año bisiesto')
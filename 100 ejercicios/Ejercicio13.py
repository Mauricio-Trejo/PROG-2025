# Convertir una temperatura entre distintas escalas

'''temp = float(input('Ingresa la temperatura en celsius:'))

tFar = temp*9/5+32
tKelvin = temp + 273.15

print('Celsius: ', temp)
print('Fahrenheit: ', tFar)
print('Kevin: ', tKelvin)'''

opt = 0

while(opt != 4):
    print('Ingresa la unidad de temperatura')
    opt = int(input('ESCOGE UNA OPCIÓN:\n1.Celsius\n2.Fahrenheit\n3.Kelvin\n4.Salir\n=>'))
    if opt == 1:
        opt2 = int(input('ESCOGE UNA OPCIÓN:\n1.Convertir a Fahrenheit\n2.Convertir a Kelvin\n3.Salir\n=>'))
        if opt2 == 3:
            pass
        else:
            temp = float(input('Ingresa la temperatura: '))
            print('Celsius: ', temp)
            if opt2 == 1:
                temp2 = temp*9/5+32
                print('Fahrenheit: ', temp2)
            elif opt2 == 2:
                temp2 = temp + 273.15
                print('Kelvin: ', temp2)
    if opt == 2:
        opt2 = int(input('ESCOGE UNA OPCIÓN:\n1.Convertir a Celsius\n2.Convertir a Kelvin\n3.Salir\n=>'))
        if opt2 == 3:
            pass
        else:
            temp = float(input('Ingresa la temperatura: '))
            print('Fahrenheit: ', temp)
            if opt2 == 1:
                temp2 = (temp - 32)*5/9
                print('Celsius: ', temp2)
            elif opt2 == 2:
                temp2 = ((temp - 32)*5/9) + 273.15
                print('Kelvin: ', temp2)
    if opt == 3:
        opt2 = int(input('ESCOGE UNA OPCIÓN:\n1.Convertir a Celsius\n2.Convertir a Fahrenheit\n3.Salir\n=>'))
        if opt2 == 3:
            pass
        else:
            temp = float(input('Ingresa la temperatura: '))
            print('Kelvin: ', temp)
            if opt2 == 1:
                temp2 = temp - 273.15
                print('Celsius: ', temp2)
            elif opt2 == 2:
                temp2 = (temp - 273.15)*9/5+32
                print('Fahrenheit: ', temp2)
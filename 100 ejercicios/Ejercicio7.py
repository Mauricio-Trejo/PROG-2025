#Determinar si un número es par, impar o múltiplo de otro

num = int(input("Ingresa un número: "))
multiplos = ['Es un número primo']

if num % 2 == 0:
    print(num, ' es un número par')
else:
    print(num, ' es un número impar')

for x in range(2, num):
    if num % x == 0:
        multiplos.append(x)

if len(multiplos) >=2:
    multiplos.remove(multiplos[0])

print('Multliplos de ', num,': ', multiplos)  
        
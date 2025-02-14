#Verificar si un número es primo

num = int(input("Ingresa un número para verificar si es primo: "))
contador = 0

for x in range(1, num+1):
    if num % x == 0:
        contador += 1

if contador == 2:
    print(num, ' es número primo')
else:
    print(num, ' NO es número primo')
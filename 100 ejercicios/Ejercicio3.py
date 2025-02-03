#Genera el factorial de un número dado

num = int(input("Ingresa un número mayor que cero para calcular su factorial: "))
factorial = 1

while num <= 0:
    print("Error: el número debe de ser mayor a cero")
    num = int(input("Ingresa un número mayor que cero para calcular su factorial: "))

for i in range(num, 1, -1):
    factorial = factorial * i

print('El factorial de ', num,' es: ', factorial)
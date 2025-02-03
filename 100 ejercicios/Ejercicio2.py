#Crear una calculadora simple que realice operaciones básicas

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

#Suma
suma = num1 + num2
#Resta
resta = num1 - num2
#Multiplicación
multi = num1 * num2

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multi)

try:
    divi = num1 / num2
    print("La división es: ", divi)
except ZeroDivisionError:
    print("No se puede dividir entre cero...")

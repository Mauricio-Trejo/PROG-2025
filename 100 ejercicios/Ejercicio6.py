#Calcular un interés compuesto dado un capital, tasa y tiempo

tasa = float(input("Ingresa la tasa de interés anual: "))
capital = float(input("Ingresa el capital inicial a invertir: "))
tiempo = float(input("Ingresa el número de años estimados a invertir: "))

tasa = tasa / 100
interes = capital * (tasa + 1)**tiempo

print("El interés compuesto a ",tiempo, " años será: ", interes)

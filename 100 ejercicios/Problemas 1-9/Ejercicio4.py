#Generar la secuencia Fibonacci hasta un número dado de términos

lim = int(input("Ingresa el número de términos que deseas ver de la secuencia Fibonacci: "))

lista = list()

for x in range(lim):
    if x == 0 or x == 1:
        lista.append(x)
        #print(lista[x])
    else:
        lista.append(lista[x-2] + lista[x-1])
        #print(lista[x])

print(lista)

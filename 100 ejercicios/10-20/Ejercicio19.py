import random

def generar_uniforme(n, a, b):
    """ Genera n números con distribución uniforme continua entre a y b """
    return [random.uniform(a, b) for _ in range(n)]

def generar_entero_uniforme(n, a, b):
    """ Genera n números enteros con distribución uniforme discreta entre a y b """
    return [random.randint(a, b) for _ in range(n)]

def generar_normal(n, media, desviacion):
    """ Genera n números con distribución normal (Gaussiana) """
    return [random.gauss(media, desviacion) for _ in range(n)]

def generar_exponencial(n, lambd):
    """ Genera n números con distribución exponencial """
    return [random.expovariate(lambd) for _ in range(n)]

def generar_triangular(n, a, b, modo):
    """ Genera n números con distribución triangular """
    return [random.triangular(a, b, modo) for _ in range(n)]

def mostrar_numeros(datos, titulo):
    """ Muestra los números generados en la consola """
    print(f"\n{titulo}:")
    print(datos)

def main():
    print("Distribuciones de números aleatorios con random:")
    print("1. Uniforme continua")
    print("2. Enteros uniformes")
    print("3. Normal (Gaussiana)")
    print("4. Exponencial")
    print("5. Triangular")
    
    opcion = int(input("Elige una distribución (1-5): "))
    n = int(input("¿Cuántos números quieres generar? "))

    if opcion == 1:
        a = float(input("Ingresa el límite inferior: "))
        b = float(input("Ingresa el límite superior: "))
        datos = generar_uniforme(n, a, b)
        mostrar_numeros(datos, f"Uniforme continua [{a}, {b}]")
    elif opcion == 2:
        a = int(input("Ingresa el límite inferior (entero): "))
        b = int(input("Ingresa el límite superior (entero): "))
        datos = generar_entero_uniforme(n, a, b)
        mostrar_numeros(datos, f"Uniforme discreta (enteros) [{a}, {b}]")
    elif opcion == 3:
        media = float(input("Ingresa la media: "))
        desviacion = float(input("Ingresa la desviación estándar: "))
        datos = generar_normal(n, media, desviacion)
        mostrar_numeros(datos, f"Normal (media={media}, desv.={desviacion})")
    elif opcion == 4:
        lambd = float(input("Ingresa el parámetro lambda (> 0): "))
        datos = generar_exponencial(n, lambd)
        mostrar_numeros(datos, f"Exponencial (λ={lambd})")
    elif opcion == 5:
        a = float(input("Ingresa el límite inferior: "))
        b = float(input("Ingresa el límite superior: "))
        modo = float(input("Ingresa el valor modal (más frecuente): "))
        datos = generar_triangular(n, a, b, modo)
        mostrar_numeros(datos, f"Triangular [{a}, {b}, modo={modo}]")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()

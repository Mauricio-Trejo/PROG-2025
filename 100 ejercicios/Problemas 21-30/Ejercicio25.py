import numpy as np
import matplotlib.pyplot as plt

def generar_datos(cantidad, media=50, desviacion=15):
    """Genera una muestra de datos con distribución normal."""
    return np.random.normal(media, desviacion, cantidad)

def graficar_histograma(datos, bins=10):
    """Genera y muestra un histograma de los datos."""
    plt.hist(datos, bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def analizar_datos(datos):
    """Calcula y muestra estadísticas básicas de los datos."""
    print(f"Media: {np.mean(datos):.2f}")
    print(f"Mediana: {np.median(datos):.2f}")
    print(f"Desviación estándar: {np.std(datos):.2f}")
    print(f"Mínimo: {np.min(datos)}")
    print(f"Máximo: {np.max(datos)}")

if __name__ == "__main__":
    cantidad_datos = int(input("Ingrese la cantidad de datos a generar: "))
    datos = generar_datos(cantidad_datos)
    graficar_histograma(datos)
    analizar_datos(datos)

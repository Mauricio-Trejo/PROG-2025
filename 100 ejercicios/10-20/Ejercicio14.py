# Función para Bubble Sort
def bubble_sort(arr):
    n = len(arr)  # Obtener la longitud del arreglo
    # Recorrer el arreglo varias veces
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Comparar el elemento actual con el siguiente
            if arr[j] > arr[j+1]:
                # Si están en el orden incorrecto, intercambiarlos
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Función para Selection Sort
def selection_sort(arr):
    n = len(arr)  # Obtener la longitud del arreglo
    # Recorrer todo el arreglo
    for i in range(n):
        min_idx = i  # Suponer que el elemento actual es el menor
        # Buscar el mínimo en el resto del arreglo
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Actualizar el índice del menor
        # Intercambiar el mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Función para Insertion Sort
def insertion_sort(arr):
    # Comienza desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual a insertar en la parte ordenada
        j = i - 1
        # Mover elementos mayores a la derecha para hacer espacio
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Colocar el elemento en su posición correcta
        arr[j + 1] = key
    return arr

# Función para Merge Sort
def merge_sort(arr):
    # Si el arreglo tiene más de un elemento, se divide
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontrar el punto medio
        L = arr[:mid]  # Dividir la mitad izquierda
        R = arr[mid:] # Dividir la mitad derecha

        # Llamada recursiva para dividir más hasta llegar a un solo elemento
        merge_sort(L)
        merge_sort(R)

        # Inicializar los índices para fusionar
        i = j = k = 0

        # Fusionar las dos mitades
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Verificar si quedaron elementos en la mitad izquierda
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Verificar si quedaron elementos en la mitad derecha
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# Función principal del programa
def main():
    # Mostrar las opciones de métodos de ordenamiento
    print("Métodos de Ordenamiento:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    
    # Solicitar al usuario que elija un método de ordenamiento
    choice = int(input("Elige el método de ordenamiento (1-4): "))

    # Solicitar al usuario que ingrese una lista de números
    arr = list(map(int, input("Ingresa los números a ordenar separados por espacio: ").split()))

    # Ejecutar el método de ordenamiento elegido
    if choice == 1:
        sorted_arr = bubble_sort(arr)
        print("Ordenado con Bubble Sort:", sorted_arr)
    elif choice == 2:
        sorted_arr = selection_sort(arr)
        print("Ordenado con Selection Sort:", sorted_arr)
    elif choice == 3:
        sorted_arr = insertion_sort(arr)
        print("Ordenado con Insertion Sort:", sorted_arr)
    elif choice == 4:
        sorted_arr = merge_sort(arr)
        print("Ordenado con Merge Sort:", sorted_arr)
    else:
        print("Opción no válida.")

# Comienza la ejecución del programa
if __name__ == "__main__":
    main()

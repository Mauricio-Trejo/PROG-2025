import vehiculos

def menu():
    print("1. Registrar Vehículo")
    print("2. Mostrar Vehículos")
    print("3. Buscar Vehículo por Marca")
    print("4. Calcular Promedio de Precios")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        precio = float(input("Ingrese el precio del vehículo: "))
        vehiculos.sistema.registrar_vehiculo(marca, modelo, precio)
        print(f"Vehículo {marca} {modelo} registrado con éxito.")
    elif opcion == 2:
        mostrar_vehiculos()
    elif opcion == 3:
        buscar_vehiculo()
    elif opcion == 4:
        calcular_promedio_precio()
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")

def mostrar_vehiculos():
    vehiculos_list = vehiculos.sistema.mostrar_vehiculos()
    if vehiculos_list:
        for vehiculo in vehiculos_list:
            print(vehiculo.mostrar_info())
    else:
        print("No hay vehículos registrados.")

def buscar_vehiculo():
    marca = input("Ingrese la marca del vehículo a buscar: ")
    encontrados = vehiculos.sistema.buscar_vehiculo(marca)
    if encontrados:
        for v in encontrados:
            print(v.mostrar_info())
    else:
        print(f"No se encontró ningún vehículo de la marca {marca}.")

def calcular_promedio_precio():
    promedio = vehiculos.sistema.calcular_promedio_precio()
    if promedio:
        print(f"Promedio de precios de los vehículos: ${promedio:.2f}")
    else:
        print("No hay vehículos registrados para calcular el promedio.")

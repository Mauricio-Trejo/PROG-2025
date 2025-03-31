class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} - Precio: ${self.precio}"

class SistemaVehiculos:
    def __init__(self):
        self.vehiculos = []

    def registrar_vehiculo(self, marca, modelo, precio):
        vehiculo = Vehiculo(marca, modelo, precio)
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.mostrar_info())

    def buscar_vehiculo(self, marca):
        encontrados = [v for v in self.vehiculos if v.marca.lower() == marca.lower()]
        if encontrados:
            for v in encontrados:
                print(v.mostrar_info())
        else:
            print(f"No se encontró ningún vehículo de la marca {marca}.")

    def calcular_promedio_precio(self):
        if self.vehiculos:
            total_precio = sum([v.precio for v in self.vehiculos])
            return total_precio / len(self.vehiculos)
        return 0

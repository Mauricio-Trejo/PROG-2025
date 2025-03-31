'''
SISTEMA DE GESTIÓN DE VEHÍCULOS.

Crea una clase vehículo con los siguientes atributos y métodos:
* Atributos: marca, modelo, año y precio.
* Método para mostrar la información del vehículo.
* Crear subclases Automovil y Motocicleta con atributos adicionales
como número de puertas o cilindrada.
'''

class vehiculo:
    def __init__(self, marca, modelo, year, precio): # Constructor inicializar los atributos
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.precio = precio
    
    def mostrar_info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.year}, Precio: ${self.precio:.2f}'

class automovil(vehiculo):
    def __init__(self, marca, modelo,year, precio, num_puertas):
        super().__init__(marca, modelo,year, precio)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        return f'{super().mostrar_info()}, Número de puertas: {self.num_puertas}'
    
class motocicleta(vehiculo):
    def __init__(self, marca, modelo, year, precio, cilindrada):
        super().__init__(marca, modelo,year, precio)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        return f'{super().mostrar_info()}, Cilindrada: {self.cilindrada}cc'


# Prueba de escritorio
auto = automovil("Toyota", "Corolla", 2022, 25000, 4)
moto = motocicleta("Honda", "CBR600RR", 2021, 12000, 600)

print(auto.mostrar_info())
print(moto.mostrar_info())

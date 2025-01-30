#tipos de datos simples
int()
str()
float()

#tipos de datos estructurados
list()
set()
tuple()
dict()

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

#tipos de datos estructurados compuestos
enumerate(meses)
#range()

for mes in enumerate(meses, 1):
    print(mes)

for j in range(0, 14, 2):
    print(j)



''' Operaciones:

Aritméticos
(x)
x**2
x * y
x / y
x + y
x - y

Lógica
and
or
not

Relacionales
<> x < y o x > y
<= >= x <= y x >= y
== x == s
!= <,>

Aritmeticos complementarios
x // y (div)
y % x (mod)


Contracciones aritmeticas
x += 1
x -= 2
y *= 1/7
y /= 7



'''

def nombrefuncion():
    print("Hola mundo desde función")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

nombrefuncion()
print(suma(5, 7))
print(resta(3, 1))
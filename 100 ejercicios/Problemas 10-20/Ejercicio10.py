#Leer, escribir y modificar un archivo de texto

#Método 1

with open('doc1.txt', 'w') as variable1:
    print('Hola mundo, se creó desde Python un archivo de texto', file = variable1)

#Método 2
'''
variable2 = open('doc2.txt', 'w')
print('Hola mundo desde Python, archivo de texto creado', file=variable2)

variable2.close()
'''
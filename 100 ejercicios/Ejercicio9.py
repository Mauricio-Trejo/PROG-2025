#Genera una lista de pares e impares hasta un límite dado

limite = int(input('Ingresa un límite: '))

par = list()
impar = list()

for num in range(1, limite+1):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
tamanio = max(len(par), len(impar))

for item in range(tamanio):
    try:
        print(par[item], impar[item])
    except IndexError:
        print('-', impar[item])

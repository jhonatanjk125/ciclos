"""
Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

"""
number = int(input('Ingrese un número: '))
for i in range(number+1):
    print(f'{2**(i)}', end=' ')
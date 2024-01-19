"""
Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

"""
height = int(input('Altura:'))

for i in range(height):
    for j in range(i+1):
        print('*', end='')
    print()
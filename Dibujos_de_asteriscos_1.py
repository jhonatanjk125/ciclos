"""
Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

"""
height = int(input('Altura:'))
width = int(input('Ancho: '))

for i in range(height):
    for j in range(width):
        print('*', end='')
    print()
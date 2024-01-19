"""
Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:
"""
number = int(input('Ingrese un número: '))
for i in range(10):
    print(f'{number} x {i+1} = {number*(i+1)}')
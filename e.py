"""
Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
"""
import math
denominator=2
difference=1
euler = 2
previous_fraction = 1
fraction = 1
while difference>0.0001:
    previous_fraction = fraction
    fraction= 1/math.factorial(denominator)
    denominator += 1
    euler += fraction
    difference= previous_fraction-fraction
print(euler)
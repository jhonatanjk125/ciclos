"""
Escriba un programa que entregue todos los divisores del número entero ingresado:

"""
number = int(input('Ingrese número: '))
divisors = []
for i in range(1,int(number**0.5)):
    if number%i==0:
        divisors.append(i)
for divisor in reversed(divisors):
    divisors.append(number/divisor)
print(divisors)
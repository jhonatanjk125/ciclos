"""
Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

"""
number1= int(input('Ingre num: '))
number2= int(input('Ingrese num: '))
sum=0
for i in range(number1+1,number2):
    sum += i
print(f'La suma es {sum}')
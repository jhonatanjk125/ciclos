"""
Desarrolle un programa que permita trabajar con las potencias fraccionales de dos
"""
fraction=1
i = 1
sum=0
headers = ['Potencia', 'Fracción', 'Suma']
for header in headers:
    print(header, end=' ')
print()
while fraction>0.000001:
    fraction=1/(2**i)
    sum+=fraction
    print(str(i).ljust(8), end=' ')
    print(str(round(fraction,4)).ljust(8), end=' ')
    print(round(sum,4))
    i+=1


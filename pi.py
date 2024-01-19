"""
Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
"""
n = int(input('n: '))
sum=0
for i in range(n):
    sum+=(-1)**(i)*(1/(2*i+1))
pi = 4 * sum
print(pi)
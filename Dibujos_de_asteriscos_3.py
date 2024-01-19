"""
Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

"""
side_length=int(input('Lado: '))
final_length = side_length + 2*(side_length-1)
for i in range(side_length):
    final_string=''
    for j in range(side_length+2*i):
        final_string+='*'
    print(final_string.center(final_length))
for x in range(1,side_length):
    final_string=''
    for j in range(2,side_length+2*(side_length-x),1):
        final_string+='*'
    print(final_string.center(final_length))

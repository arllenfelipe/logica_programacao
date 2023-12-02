a = int(input('digite um valor: '))
b = int(input('digite outro valor: '))
c = int(input('digite outro valor: '))
d = int(input('digite outro valor: '))
if (b > c) and (d > a) and (c + d > a + b) and (c > 0) and (d > 0) and (a % 2 == 0) :
    print('Valores aceitos')
else:
    print('Valores não aceitos')
 


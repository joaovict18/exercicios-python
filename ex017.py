from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comrpimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))

# também é possível utilizar o sqt(x*x + y*y)

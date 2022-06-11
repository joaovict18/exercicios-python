'''from math import factorial
print('Digite um número para')
número = int(input('calcular seu Fatorial: '))
print('O fatorial de {} é {}.'.format(número, factorial(número)))'''

'''n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c, end=' '))
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Digite um número para ver seu fatorial: '))
f = 1
for c in range(1, n):
    f = 1
    c -= 1
print(f)
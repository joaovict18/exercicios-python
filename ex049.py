n = int(input('Digite um número para ver sua tabuada: '))
for t in range(1, 11):
    print('{} x {:2} = {}'.format(n, t, n * t))
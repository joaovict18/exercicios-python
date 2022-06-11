# para o cálculo da raiz, pode-se usar a função sqrt do módulo math
num = int(input('Digite um número: '))
print('O dobro de \033[35m{}\033[m vale \033[35m{}\033[m.' .format(num,(num * 2)))
print('O triplo de \033[36m{}\033[m vale \033[36m{}\033[m.' .format(num,(num * 3)))
rq = num ** (1/2)
print('A raiz quadrada de \033[33m{}\033[m vale \033[33m{:.2f}\033[m.' .format(num,rq))

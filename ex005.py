num = int(input('Digite um número: '))
print('Analisando o valor \033[31m{}\033[m, seu antecessor é \033[33m{}\033[m e o sucessor é \033[32m{}\033[m' .format(num,(num - 1),(num + 1)))

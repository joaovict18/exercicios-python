nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
print('A média entre \033[31m{}\033[m e \033[31m{}\033[m é igual a \033[32m{:.1f}\033[m' .format(nota1,nota2,((nota1 + nota2) / 2)))

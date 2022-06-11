nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
média = (nota_1 + nota_2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota_1, nota_2, média))
if média < 5:
    print('O aluno está REPROVADO.')
elif média >= 5 and média < 7:
    print('O aluno está de RECUPERAÇÃO.')
elif média >= 7:
    print('O aluno está APROVADO.')

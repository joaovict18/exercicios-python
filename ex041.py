from datetime import date
ano_de_nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - ano_de_nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')

# também é possível fazer sem a primeira condição, sendo o operador de maior que a idade citada anteriormente

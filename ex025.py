'''nome = str(input('Qual é seu nome completo? ')).strip()
nome_maiúsculo = nome.upper()
achador = 'SILVA' in nome_maiúsculo
print(f'Seu nome tem Silva? {achador}')'''

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('É um prazer te conhecer!')
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[-1])) #ou nome[len(nome)-1]

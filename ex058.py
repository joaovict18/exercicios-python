from random import randint
número = randint(1, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palpite = 0
tentativas = 0
while palpite != número:
    palpite = int(input('Qual seu palpite? '))
    if palpite < número:
        print('Mais... Tente mais uma vez.')
        if palpite != número: tentativas += 1
    if palpite > número:
        print('Menos... Tente mais uma vez.')
        if palpite != número: tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas + 1))

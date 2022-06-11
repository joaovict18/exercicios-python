from random import randint
from time import sleep # O sleep faz com que o computador demore um pouco à responder
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
resposta = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
# sleep(3)
número = randint(0, 5)
if resposta == número:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(número, resposta))

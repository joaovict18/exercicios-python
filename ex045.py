from time import sleep
from random import randint
lista_de_opções = ('Pedra', 'Papel', 'Tessoura')
escolha_do_computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESSOURA''')
escolha = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}'.format(lista_de_opções[escolha_do_computador]))
print('Jogador jogou {}'.format(lista_de_opções[escolha]))
if escolha == 0: # jogador escolheu pedra
    if escolha_do_computador == 0:
        print('EMPATE')
    elif escolha_do_computador == 1:
        print('COMPUTADOR VENCE')
    elif escolha_do_computador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if escolha == 1: # jgoador escolheu papel
    if escolha_do_computador == 0:
        print('JOGADOR VENCE')
    elif escolha_do_computador == 1:
        print('EMPATE')
    elif escolha_do_computador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if escolha == 2: # jogador escolheu tessoura
    if escolha_do_computador == 0:
        print('COMPUTADOR VENCE')
    elif escolha_do_computador == 1:
        print('JOGADOR VENCE')
    elif escolha_do_computador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print('-=' * 12)

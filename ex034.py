salário = float(input('Qual o salário do funcionário? R$'))
if salário > 1250:
    novo = salário + (salário * 0.1)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
if salário <= 1250:
    novo = salário + (salário * 0.15)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))

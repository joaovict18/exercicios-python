# R$ 3.27
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com \033[33m{}\033[m você pode comprar US$\033[32m{:.2f}\033[m'.format(dinheiro, (dinheiro / 3.27)))

# o carro custa R$60 por dia e R$0,15 por Km rodado
x = int(input('Quanto dias alugados? '))
y = float(input('Quantos Km rodados? '))
z = x*60 + y*0.15
print('O total a pagar é de R${:.2f}'.format(z))

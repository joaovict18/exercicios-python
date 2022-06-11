x = float(input('Qual é o salário do Funcionário? R$'))
y = x+(x*0.15)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}' .format(x,y))

v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
pr = v / (a * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v, a, pr))
p = (s * 30) / 100
if pr >= p:
	print('Empréstimo NEGADO!')
else:
	print('Empréstimo pode ser CONCEDIDO!')

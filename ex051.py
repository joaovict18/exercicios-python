print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro_termo + (10 - 1) * razão
for pa in range(primeiro_termo, décimo, razão):
    print(pa, end=' → ') 
print('ACABOU')

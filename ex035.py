from time import sleep
print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segumento: '))
print('Processando...')
sleep(2)
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

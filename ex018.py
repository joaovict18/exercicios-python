'''from math import radians, sin, cos, tan

x = int(input('Digite o ângulo que você deseja: '))
seno = radians(x)
print('O ângulo de {} tem o SENO de {:.2f}' .format(x, sin(seno)))
cosseno = radians(x)
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(x, cos(cosseno)))
tangente = radians(x)
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(x, tan(tangente)))'''

from math import radians, sin, cos, tan

x = int(input('Digite o ângulo que você deseja: '))
rad = radians(x)
print('O ângulo de {} tem o SENO de {:.2f}' .format(x, sin(rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(x, cos(rad)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(x, tan(rad)))

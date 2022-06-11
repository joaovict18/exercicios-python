nome = str(input('Digite seu nome completo: ')) # pode-se utilizar o strip na variável direto para cortar os espaços inúteis
print('Analisando seu nome...')
print('Seu nome em maiúsculas é \033[34m{}\033[m'.format(nome.upper()))
print('Seu nome em minúsculas é \033[36m{}\033[m'.format(nome.lower()))
nome_sem_espaços = ''.join(nome.split()) # também é possível retirar os espaços diminuindo sobre o mesmo e contando os espaços com o cout
print('Seu nome tem ao todo \033[33m{}\033[m letas'.format(len(nome_sem_espaços))) 
separa = nome.split()
print('Seu primeiro nome é \033[32m{}\033[m e ele tem \033[31m{}\033[m letras'.format(separa[0], len(separa[0])))

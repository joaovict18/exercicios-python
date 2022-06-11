from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {} + {} é {}'.format(primeiro_valor, segundo_valor, primeiro_valor + segundo_valor))
        print('=-==' * 9)
        sleep(2)
    elif opção == 2:
        print('O resultado de {} + {} é {}'.format(primeiro_valor, segundo_valor, primeiro_valor * segundo_valor))
        print('-==' * 9)
        sleep(2)
    elif opção == 3:
        if primeiro_valor > segundo_valor:
            print('Entre {} e {} o maior valor é {}'.format(primeiro_valor, segundo_valor, primeiro_valor))
        else:
            print('Entre {} e {} o maior valor é {}'.format(primeiro_valor, segundo_valor, segundo_valor))
            print('-==' * 9)
            sleep(2)
    elif opção == 4:
        print('Informe os números novamente: ')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
        print('-==' * 9)
        sleep(2)
    elif opção == 5:
        print('Finalizando...')
        print('-==' * 9)
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
        print('-==' * 9)
        sleep(2)
print('Fim do programa! Volte sempre!')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
option = 0
while option!=5:
    print('\nO que você deseja fazer: ')
    option=int(input('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NUMEROS\n[ 5 ] SAIR\n'))
    if option == 1:
        print('A soma deles é {}'.format(num1+num2))
    elif option == 2:
        print('O produto entre os numeros é {}'.format(num1*num2))
    elif option == 3:
        if num1>num2:
            print('O maior numero é {}'.format(num1))
        elif num1< num2:
            print('O maior numero é {}'.format(num2))
        else:
            print('Os numeros são iguais')
    elif option == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif option == 5:
        print('FIM')
    else:
        print('Opção inválida')
def leiaint(msg):
    bol = False
    value = 0
    while True:
        x = str(input(msg))
        if x.isnumeric():
            value = int(x)
            bol = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido\033[m')
        if bol:
            break
    return value


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
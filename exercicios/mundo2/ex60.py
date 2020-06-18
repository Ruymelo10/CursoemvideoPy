num = int(input('Você deseja saber o fatorial de que numero: '))
print('Calculando {}! = '.format(num), end='')
cont = num
fat = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont>1 else ' = ', end='')
    fat*=cont
    cont-=1
print(fat)
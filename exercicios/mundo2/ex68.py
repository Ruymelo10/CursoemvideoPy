from random import randint
cont = 0
print('*'*15, end=' ')
print('PAR OU ÍMPAR', end=' ')
print('*'*15)
while True:
    opc = str(input('')).strip().lower()
    num = int(input('Quantos deseja colocar? '))
    pc = randint(1,20)
    soma = num+ pc
    if opc == 'par':
        if soma%2==0:
            print(f'\033[31m{soma}\033[m. Parabéns!')
            cont+=1
        else:
            print(f'\033[31m{soma}\033[m. Você perdeu :(')
            break
    elif opc == 'impar':
        if soma%2 !=0:
            print(f'\033[31m{soma}\033[m. Parabéns!')
            cont += 1
        else:
            print(f'\033[31m{soma}\033[m. Você perdeu :(')
            break
print('*'*15, end=' ')
print('FIM DE JOGO', end=' ')
print('*'*16)
print(f'Seu total de vitórias foi \033[33m{cont}\033[m')




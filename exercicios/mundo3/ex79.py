list = []
while True:
    num = int(input('Digite um numero: '))
    if num not in list:
        list.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar')
    cont = input('Deseja continuar? [S/N]')
    if cont in 'Nn':
        break
list.sort()
print('-='*25)
print(f'A sua lista foi {list}')
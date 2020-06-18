from random import randint
tup = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os numeros sorteados foram', end=' ')
for i in tup:
    print(f'{i}',end=' ')
print(f'\nO maior valor foi {max(tup)}')
print(f'O menor valor foi {min(tup)}')
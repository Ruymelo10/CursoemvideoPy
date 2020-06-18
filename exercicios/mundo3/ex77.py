pal=('UMA','BESTA','ENJAULADA','COM','ODIO','SEU','FILHA', 'DA',
     'PUTA','ELE','VENCE','E','VENCE')
for i in pal:
    print(f'\nNa palavra {i} temos ', end='')
    for c in i:
        if c in 'AEIOU':
            print(f'{c} ', end='')
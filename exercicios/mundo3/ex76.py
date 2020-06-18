listagem =('Pão', 1.50, 'Presunto',1.90,'Arroz',2.00,'Sal',1.3,
           'Pringles', 12.00,'Café', 4.50,'Refrigerante', 9.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0,len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<32}', end='')
    else:
        print(f'R${listagem[i]:>6.2f}')
print('-'*40)
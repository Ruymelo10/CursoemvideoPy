maior = 0
menor = 999
for i in range(1,6):
    c = float(input('Informe o peso da {}ª pessoa: '.format(i)))
    if c>maior:
        maior=c
    if c<menor:
        menor=c
print('O menor peso foi {}kg, e o maior foi {}kg'.format(menor,maior))
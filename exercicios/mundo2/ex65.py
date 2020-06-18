cont = 's'
count = media = sum = 0
while cont not in 'Nn':
    num = int(input('Digite um numero: '))
    count+=1
    if count == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor=num
    sum = sum+num
    media = sum/count
    cont=str(input('Deseja continuar? [S/N]')).strip()
print('Você digitou {} numeros e a media foi {}'.format(count,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
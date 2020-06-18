from datetime import date
maior = 0
menor=0
for i in range(1,8):
    c = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(i)))
    if date.today().year - c >18:
        maior+=1
    else:
        menor+=1
print('Exismte {} maiores de idade e {} menores de idade'.format(maior,menor))
media=0
idanterior = 0
velhaço = ''
novinhas = 0
for i in range(1,5):
    a = str(input('Informe o nome da {}ª pessoa: '.format(i)))
    b = int(input('Agora a sua idade: '))
    c = str(input('Por fim, seu sexo(M ou F): '))
    media+=b
    if i == 4:
        media=media/4
    if c=='M':
        if b>idanterior:
            velhaço = a
            idanterior=b
    if c == 'F' and b<20:
        novinhas+=1
print('A media de idade é {}. O mais velho é {}, e tem {} mulheres com menos de 20 anos'.format(media,velhaço,novinhas))
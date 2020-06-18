nota1 = float(input('Digite sua primeria nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
print('Sua média é {:.2f}. Você está '.format(media), end='')
if media >= 7:
    print('APROVADO')
elif media > 5:
    print('DE RECUPERAÇÃO')
else:
    print('REPROVADO')
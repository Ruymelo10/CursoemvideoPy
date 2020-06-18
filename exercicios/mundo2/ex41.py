from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print('Sua categoria é: ')
if idade > 20:
    print('Master')
elif idade > 19:
    print('Senior')
elif idade > 14:
    print('Junior')
elif idade > 9 :
    print('Infantil')
else:
    print('Mirim')
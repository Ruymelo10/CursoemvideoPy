import datetime
nasc = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual-nasc
if idade < 18:
    print('Ainda não está na hora de se alistar. ', end='')
    print('Ainda faltam {} anos'.format(18-idade))
elif idade > 18:
    print('Já passou da hora de se alistar.', end='')
    print(' Seu alistamento foi há {} anos'.format(idade-18))
else:
    print('Tá na hora de se alistar')
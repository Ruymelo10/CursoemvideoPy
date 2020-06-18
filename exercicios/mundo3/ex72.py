num = ('zero','um', 'dois', 'tres','quatro', 'cinco','seis','sete','oito','nove','dez',
       'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito',
       'dezenove','vinte')
while True:
    esco = int(input('Digite um numero entre 0 e 20: '))
    if 0<=esco<=20:
        break
    else:
        print('Tente novamente.',end=' ')

print(f'Você escolheu o numero {num[esco]}')


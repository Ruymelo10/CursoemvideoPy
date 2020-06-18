from random import randint
print('Tente advinhar o numero que o computador pensou')
num = int(input('Digite um numero de 1 a 10: '))
pc = randint(1,10)
count = 1
while num!=pc:
    print('Você errou. Tente novamente')
    num = int(input('Digite um numero de 1 a 10: '))
    count+=1
print('Agora sim! O computador escolheu {} e você digitou {}.'.format(pc,num))
print('Foram necessárias {} tentativas'.format(count))
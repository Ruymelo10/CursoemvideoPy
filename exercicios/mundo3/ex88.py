from time import sleep
from random import randint
print('='*30)
print(f'{"MEGA SENA":^30}')
print('='*30)
jogos = int(input('Quanto jogos você quer que eu sorteie? '))
print('SORTEANDO JOGOS')
lista = list()
cartela = list()

for i in range(jogos):
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>5:
            break
    lista.sort()
    cartela.append(lista[:])
    lista.clear()
print('-='*5,'SORTEANDO OS JOGOS','-='*5)
for i,l in enumerate(cartela):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

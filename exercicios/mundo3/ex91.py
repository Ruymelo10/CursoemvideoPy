from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Joador 1':randint(1,6),
           'Joador 2':randint(1,6),
           'Joador 3':randint(1,6),
           'Joador 4':randint(1,6)}
for k,v in jogadas.items():
    print(f'{k} tirou {v}')
ordem = sorted(jogadas.items(),key=itemgetter(1), reverse=True)
for x,y in enumerate(ordem):
    print(f'{x+1}º lugar: {y[0]} que tirou {y[1]}')

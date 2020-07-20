from random import randint


def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ',end='')
    for i in range(0,5):
        x= randint(1,10)
        lista.append(x)
        print(f'{x} ', end='', flush=True)
    print('PRONTO!') 


def somaPar(lista):
    soma=0
    for i in lista:
        if i % 2 == 0:
          soma+=i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros)
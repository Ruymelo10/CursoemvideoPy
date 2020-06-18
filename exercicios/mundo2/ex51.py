p = int(input('Digite o primeiro numero da PA: '))
r = int(input('Informe a razão da sua PA: '))
numAtual = p
for i in range(p, p+(10*r), r):
    if i==p:
        print(numAtual, end=' ')
    else:
        numAtual+=r
        print(numAtual, end=' ')


p = int(input('Digite o primeiro numero da PA: '))
r = int(input('Informe a razão da sua PA: '))
cont = 9
extra=1
while extra != 0:
    cont+=extra
    while cont > 0 :
        if cont != 10:
            p=p+r
        print(p, end=' ')
        cont-=1
    extra = int(input('\nVocê deseja ver mais quantos termos: '))


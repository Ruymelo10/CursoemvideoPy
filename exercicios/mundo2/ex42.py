a1 = float(input('Digite o primeiro segmento: '))
a2 = float(input('Digite o segundo segmento: '))
a3 = float(input('Digite o terceiro segmento: '))

if a1<a2+a3 and a2<a1+a3 and a3<a1+a2:
    print('Os segmentos acima podem formar um triangulo. ', end='')
    if a1==a2==a3:
        print('Ele é EQUILATERO')
    elif a1==a2 or a2==a3 or a1==a3:
        print('Ele é ISOCELES')
    else:
        print('Ele é ESCALENO')
else:
    print('Os segmentos acima NÃO podem formar um triangulo')
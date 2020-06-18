parcial = 0
print('{:^40}'.format('BANCO DA GAMA'))
print('='*40)
saque = int(input('QUal o valor a ser sacado? R$'))
cinq = vinte = dez = um = 0
while parcial!=saque:
    dif = saque - parcial
    if dif>50:
        parcial+=50
        cinq+=1
    elif dif>20:
        parcial+=20
        vinte+=1
    elif dif>10:
        parcial+=10
        dez+=1
    else:
        parcial+=1
        um+=1

print(f'Total de cedulas de R$50: {cinq}')
print(f'Total de cedulas de R$20: {vinte}')
print(f'Total de cedulas de R$10: {dez}')
print(f'Total de cedulas de R$1: {um}')
print('='*40)


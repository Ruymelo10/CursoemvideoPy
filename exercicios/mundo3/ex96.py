def area(larg, comp):
    tot = larg*comp
    return tot


print('Controle de terrenos')
print('-'*25)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
print(f'A área de um terreno {l}x{c} é de {area(l,c)}m²')

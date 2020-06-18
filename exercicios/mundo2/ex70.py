total=caros=rspechincha=0
pechincha = ' '
while True:
    print('='*40)
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    parada = str(input('Deseja continuar? [S/N]')).strip().upper()
    if total == 0:
        pechincha = nome
        rspechincha = preco
    total+=preco
    if preco > 1000:
        caros+=1
    if preco < rspechincha:
        pechincha = nome
    print('='*40)
    if parada =='N':
        break
print(f'O gasto total é R${total:.2f}. O produto mais barato é {pechincha} e '
      f'existem {caros} produtos que custam mais de R$1000')

num = [[],[]]
for i in range(1,8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor%2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(num)
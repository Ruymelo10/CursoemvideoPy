num=[]
pares=[]
impares=[]
while True:
    x = int(input('Digite um numero: '))
    num.append(x)
    if x%2==0:
        pares.append(x)
    else:
        impares.append(x)
    cond=' '
    while cond not in 'SsNn':
        cond = str(input('Deseja continuar [S/N]? '))
    if cond in 'nN':
        break
print(f'A lista de todos os numeros é {num}')
print(f'A lista de numeros pares é {pares}\nA lista de numeros impares é {impares}')

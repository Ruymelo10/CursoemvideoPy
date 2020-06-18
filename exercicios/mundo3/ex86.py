matriz=[[],[],[]]
pares = col3 = mai2 = 0
for l in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite o valor da [{l},{c}]: '))
        if num%2==0:
            pares+=num
        if c == 2:
            col3+=num
        if l == 1:
            if mai2 < num:
                mai2 = num
        matriz[l].append(num)
print(matriz)
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('=-'*30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {mai2}')
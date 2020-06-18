list=[]
for i in range(0,5):
    num = int(input('Digite um numero: '))
    if i == 0:
        list.append(num)
        print(f'Adicionando {num} na posição 0...')
    else:
        for c in range(0,len(list)+1):
            if c == len(list):
                list.append(num)
                print(f'Adicionando {num} na posição {c}...')
            elif num < list[c]:
                list.insert(c,num)
                print(f'Adicionando {num} na posição {c}...')
                break
print(list)
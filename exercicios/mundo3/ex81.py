lista =[]
cont=0
cincao=False
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    cont += 1
    parar = str(input('Deseja continuar? [S/N]'))
    if parar in 'Nn':
        break
print(f'Foram digitados {cont} numeros.\nA lista é {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista')
else:
    print(f'O valor 5 não foi digitado e não está na lista')
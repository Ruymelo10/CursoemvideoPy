from time import sleep


def maior(*num):
    maior=cont=0
    for i in num:
        print(f'{i} ',end='', flush=True)
        sleep(0.3)
        if i > maior:
            maior = i
        cont+=1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor foi {maior}')


maior(2,3,45,6)


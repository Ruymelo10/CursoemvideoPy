from time import sleep
def contagem(ini,fim,pas):
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    sleep(1)
    if pas == 0:
        pas=1
    if pas < 0:
        pas*=-1
    if fim < ini:
        if pas > 0:
            pas = -pas
        fim-=1
    else:
        fim+=1
    for i in range(ini,fim,pas):
        print(i, end=' ',flush=True)
        sleep(0.5)
    print('FIM!')

print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio,fim,passo)
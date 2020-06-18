pessoas = list()
maiorp=0
menorp=9999
while True:
    aux=list()
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    if peso > maiorp:
        maiorp = peso
    if peso < menorp:
        menorp=peso
    aux.append(nome)
    aux.append(peso)
    pessoas.append(aux)
    stop = ' '
    while stop not in 'NnSs':
        stop = str(input('Deseja parar [S/N]? '))
    if stop in 'Ss':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
pesadao = list()
levao = list()
for i in pessoas:
    if i[1] == maiorp:
        pesadao.append(i[0])
    elif i[1] == menorp:
        levao.append(i[0])
print(f'As pessoas mais pesadas são {pesadao}')
print(f'As pessoas mais leves são {levao}')
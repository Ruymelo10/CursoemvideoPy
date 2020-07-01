list_pessoas = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Favor digitar M ou F')
    pessoa['idade'] = int(input('Idade: '))
    list_pessoas.append(pessoa.copy())
    while True:
        cont = str(input('Deseja continuar? [S/N]'))
        if cont in 'NnSs':
            break
        print('Favor digite N ou S')
    if cont in 'nN':
        break
print('-='*20)
print(f'A) Ao todo temos {len(list_pessoas)} pessoas cadastradas.')
mediaidade = 0
list_mulheres = list()
for i in list_pessoas:
    mediaidade+=i['idade']
    if i['sexo'] == 'F':
        list_mulheres.append(i['nome'])
mediaidade = mediaidade/len(list_pessoas)
print(f'B) A média de idade das pessoas é de {mediaidade:.2f} anos.')
print(f'C) As mulheres cadastradas foram {list_mulheres}')
list_acimamedia = list()
for i in list_pessoas:
    if i['idade']>mediaidade:
        list_acimamedia.append(i)
print(f'D) Lista de pessoas acima da media de idade: ')
for i in list_acimamedia:
    print(f'{i["nome"]} com {i["idade"]} anos')

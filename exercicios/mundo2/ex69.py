cont = maior = homem = novinha = 0
while True:
    cont+=1
    print('-'*40)
    idade = int(input(f'Digite a idade da {cont}ª pessoa: '))
    sexo = ' '
    while sexo not in 'fFmM':
        sexo = str(input('Digite o sexo desta pessoa[F/M]: ')).strip().upper()
    if idade > 18:
        maior +=1
    if sexo == 'M':
        homem+=1
    elif idade < 20:
        novinha+=1
    parada =' '
    while parada not in 'sSNn':
        parada = str(input('Deseja continuar? [S/N]')).strip().upper()
    print('-'*40)
    if parada == 'N':
        break
print(f'Foram cadastradas {cont} pessoas')
print(f'A) Tem {maior} pessoas com mais de 18 anos')
print(f'B) Tem {homem} homens')
print(f'C) Tem {novinha} mulheres com menos de 20 anos')
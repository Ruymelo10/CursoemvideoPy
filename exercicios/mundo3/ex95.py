lista_jogadores = list()
while True:
    nome = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    aproveitamento = list()
    for i in range(1, partidas+1):
        gols = int(input(f'Quantos gols na partida {i}? '))
        aproveitamento.append(gols)
    totalgols = sum(aproveitamento)
    fichajog = {'nome':nome,'gols':aproveitamento,'total':totalgols}
    lista_jogadores.append(fichajog)
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont == 'N':
        print('-='*30)
        break
    print('--'*30)
print('cod ',end='')
for i in fichajog.keys():
    print(f'{i:<15} ', end='')
print()
for k,v in enumerate(lista_jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para terminar) ' ))
    if jog == 999:
        break
    if jog >= len(lista_jogadores):
        print(f'ERRO não existe jogador com o código {jog}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista_jogadores[jog]["nome"]}')
        for k,v in enumerate(lista_jogadores[jog]['gols']):
            print(f'    No jogo {k+1} ele fez {v} gols')


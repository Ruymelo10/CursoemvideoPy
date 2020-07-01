nome = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
aproveitamento = list()
for i in range(1, partidas+1):
    gols = int(input(f'Quantos gols na partida {i}? '))
    aproveitamento.append(gols)
totalgols = sum(aproveitamento)
fichajog = {'nome':nome,'gols':aproveitamento,'total':totalgols}
print(f'O jogador {fichajog["nome"]} jogou {partidas} partidas')
for i,v in enumerate(fichajog['gols']):
    print(f'    Na partida {i+1} fez {v} gols')
print(f'Foi um total de {fichajog["total"]} gols')
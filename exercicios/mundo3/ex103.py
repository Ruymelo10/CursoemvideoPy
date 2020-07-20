def ficha(jog,gols):
    if jog =="":
        jog ='<Desconhecido>'
    if gols =="":
        gols = 0
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato')


jogador = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
ficha(jogador,gol)

def voto(anosnasc):
    from datetime import date
    idade = date.today().year - anosnasc
    if anosnasc < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade<=16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input(f'Em que ano você nasceu? '))
print(voto(nasc))
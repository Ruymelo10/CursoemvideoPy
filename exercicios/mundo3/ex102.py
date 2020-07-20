def fatorial(num,show=False):
    """
    Calcula o fatorial de um numero
    :param num: O fatorial que você quer saber
    :param show:(opcional) Mostrar o passo a passo
    :return: O valor do fatorial do fatorial de num
    """
    fat = 1
    for i in range(num,0,-1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat*=i
    return fat
help(fatorial)
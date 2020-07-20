def notas(*n, sit=False):
    """
    Função para descrever o boletim de notas
    :param n:A(s) nota(s) do aluno
    :param sit:(Opcional) Mostra a situação atual do aluno
    :return: Dicionário com as informações
    """
    dicionario = dict()
    dicionario['Quantidade de notas'] = len(n)
    dicionario['Maior nota'] = max(n)
    dicionario['Menor nota'] = min(n)
    dicionario['Media'] = sum(n)/len(n)
    if sit:
        if dicionario['Media'] > 7:
            dicionario['Situação'] = 'Aprovado'
        elif dicionario['Media']>=5:
            dicionario['Situação'] = 'Recuperação'
        else:
            dicionario['Situação'] = 'Reprovado'
    return dicionario



resp = notas(5.5, 2.5, 8.5)
print(resp)
help(notas)
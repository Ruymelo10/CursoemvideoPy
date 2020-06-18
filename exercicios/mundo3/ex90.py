aurelio = {'nome': str(input('Nome: ')), 'media': float(input('Média: '))}
print(f'Nome é {aurelio["nome"]}, Média é {aurelio["media"]}')
if aurelio['media']<5:
    aurelio['situacao'] = 'reprovado'
elif aurelio['media']<7:
    aurelio['situacao'] = 'recuperação'
else:
    aurelio['situacao'] = 'aprovado'
print(f'A situação é {aurelio["situacao"]}')
print('-='*30)
print(aurelio)
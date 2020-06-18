coloc = ('Framengo', 'Peixão', 'Verdão elétrico', 'Gremiu', 'AtHletico',
         'Tricolor paulista', 'Colorado','Curintia','Tricolor de aço', 'Ex de michael',
         'Bahea minha porra','GIGANTESCO COLOSSO DA COLINA DA GAMA','Atletico sem H',
         'Fluzão da massa', 'Botou o bangu na roda', 'Ciará','Serie B','Azulão',
         'Chapeterror','Hawaii')
pos = coloc.index('Chapeterror')
print(f'Os 5 primeiros foram: {coloc[:5]}')
print(f'Os 4 ultimos foram {coloc[-4:]}')
print(f'Times em ordem alfabética {sorted(coloc)}')
print(f'A posição da Chapeterror é {pos+1}ª')
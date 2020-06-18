alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunos.append([nome,[nota1,nota2],media])
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'nN':
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i,o in enumerate(alunos):
    print(f'{i+1:<4}{alunos[i][0]:<10}{alunos[i][2]:>8}')
print('-='*20)
while True:
    num = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    print(f'As notas de {alunos[num-1][0]} são {alunos[num-1][1]}')

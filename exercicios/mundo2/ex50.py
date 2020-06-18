soma =0
for i in range(1,7):
    numero = int(input('Digite o {} numero: '.format(str(i)+'o')))
    if numero%2==0:
        soma +=numero
print('A soma dos numeros pares é {}'.format(soma))
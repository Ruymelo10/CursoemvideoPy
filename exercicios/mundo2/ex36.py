val = int(input('Qual o valor da casa?: R$'))
sal = int(input('Qual o seu salário?: R$'))
ans = int(input('Em quantos anos você vai pagar?: '))
prest = val/(ans*12)
print('Para pegar uma casa de {} em {} anos você precisa de uma prestação de R${:.2f}. '.format(val,ans,prest), end='')
print('30% do seu salário é {:.2f}'.format(sal*0.3))
if(sal*0.3 < prest):
    print('Emprestimo NEGADO')
else:
    print('Emprestimo ACEITO')

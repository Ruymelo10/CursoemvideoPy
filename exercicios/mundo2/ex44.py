preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] À vista dinheiro/cheque\n[ 2 ] À vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual sua opção? '))
if opcao == 1:
    print('Seu preço com 10% de desconto é {}'.format(preco*0.9))
elif opcao == 2:
    print('Seu preço com 5% de desconto é {}'.format(preco*0.95))
elif opcao == 3:
    print('Seu preço é {}'.format(preco))
elif opcao == 4:
    print('Seu preço com 20% de juros é {}'.format(preco*1.2))
else:
    print('Opção inválida. Tente novamente')
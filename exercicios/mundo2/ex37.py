
num = int(input('Digite um número: '))
print('Podemos converter este número')
print('Selecione: \n1 para BINÁRIO\n2 para OCTAL\n3 para HEXADECIMAL')
op = int(input('Digite sua opção: '))
if(op==1):
    print('{} convertido pra BINÁRIO é {}'.format(num, bin(num)[2:]))
elif(op==2):
    print('{} convertido para OCTAL é {}'.format(num,oct(num)[2:]))
elif(op==3):
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
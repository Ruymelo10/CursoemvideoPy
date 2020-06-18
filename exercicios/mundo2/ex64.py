num = int(input('Digite um número: '))
resultado = num
cont = 1
while num != 999:
    num = int(input('Some com outro: '))
    if num != 999:
        resultado+=num
        cont+=1
print('Você digitou {} numeros e o resultado final é: {}'.format(cont,resultado))


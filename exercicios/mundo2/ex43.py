from math import pow
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (pow(altura,2))
print('Seu IMC é {:.2f}. '.format(imc), end='')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal')
elif imc <30:
    print('Você está com sobrepeso')
elif imc<40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
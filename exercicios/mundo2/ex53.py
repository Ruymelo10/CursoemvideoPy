frase = input('Digite uma frase: ')
contrario =''
contrario=frase[::-1]
'''
for i in range(len(frase)-1,-1,-1):
    contrario+=frase[i]
'''
if frase.lower().replace(" ","") == contrario.lower().replace(" ",""):
    print('É palindromo')
else:
    print('Não é palindromo')
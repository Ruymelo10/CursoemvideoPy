a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
d = int(input('Digite um numero: '))
tup = (a,b,c,d)
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if 3 not in tup:
    print('O valor 3 não foi digitado')
else:
    print(f'O valor 3 apareceu na {tup.index(3)+1}ª posição')
print(f'Os valores pares digitados foram: ',end='')
for i in range(0,len(tup)):
    if tup[i]%2==0:
        print(tup[i],end=' ')
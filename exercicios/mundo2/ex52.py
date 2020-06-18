num = int(input('Digite um numero: '))
bool = True
for i in range(num,0,-1):
    if i!=num and i!=1:
        if num%i==0:
            bool=False

if bool == False:
    print('O numero {} não é primo'.format(num))
else:
    print('O numero {} é primo'.format(num))
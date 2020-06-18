n = int(input('Quanto elementos da sequencia de fibonacci voce deseja? '))
f1=1
f2=1
print('0 -> 1 -> 1 -> ', end='')
c=3
while c<n:
    f3=f1+f2
    print('{}'.format(f3), end='')
    print(' -> 'if c<n-1 else '', end='')
    f2=f1
    f1=f3
    c+=1
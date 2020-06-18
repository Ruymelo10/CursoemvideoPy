from time import sleep
print('VAI COMEÇAR O SHOW DE FOGOS!\nPREPARE-SE:')
for i in range (10,-1,-1):
    print('{}'.format(i))
    sleep(1)
    if(i==0):
        print('BOOOOOM')
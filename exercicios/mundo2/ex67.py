from time import sleep
while True:
    num = int(input('Digite a tabuada que deseja saber: '))
    if num < 0:
        break
    sleep(1)
    print('~'*30)
    for i in range (1,10,1):
        print(f'{num} x {i} = {num*i}')
    print('~'*30)
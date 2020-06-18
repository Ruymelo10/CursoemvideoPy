from random import randint
from time import sleep
import sys
print('=================== PEDRA PAPEL E TESOURA ========================')
player = int(input('Selecione:\n\033[37m[ 1 ] Pedra\033[m\n\033[30m[ 2 ] Papel\033[m\n\033[31m[ 3 ] Tesoura\033[m\n'))
pc = randint(1,3)
if player > 3 or player < 1:
    sys.exit('Opção inválida. Jogue novamente')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(0.5)
print('-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-')
sleep(0.5)
if player == 1:
    print('Você escolheu \033[37mPEDRA\033[m')
elif player == 2:
    print('Você escolheu \033[30mPAPEL\033[m')
elif player == 3:
    print('Você escolheu \033[31mTESOURA\033[m')
sleep(2)
if pc == 1:
    print('Computador escolher \033[37mPEDRA\033[m')
elif pc == 2:
    print('Computador escolheu \033[30mPAPEL\033[m')
else:
    print('Computador escolher \033[31mTESOURA\033[m')
sleep(0.2)
print('-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-=-=-')
sleep(1)
if player == pc:
    print('\033[33mEMPATE\033[m')
elif (player == 1 and pc ==3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
    print('\033[33mJOGADOR GANHOU\033[m')
else:
    print('\033[33mCOMPUTADOR GANHOU\033[m')


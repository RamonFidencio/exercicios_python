from random import randint
from time import sleep
user = int(input('1-PEDRA\n2-PAPEL\n3-TESOURA\nQUAL SUA ESCOLHA:'))
pc = int (randint(1,3))
if pc == 1:
    print('O computador escolheu PEDRA')
elif pc == 2:
    print('O computador escolheu PAPEL')
elif pc == 3:
    print('O computador escolheu TESOURA')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POH !!!\n')
sleep(1)
print('-='*20)
if user == pc:
    print('\nEMPATE')
elif user==1 and pc ==2:
    print('Você PERDEU')
elif user==1 and pc ==3:
    print('Você VENCEU')

elif user==2 and pc ==3:
    print('Você PERDEU')
elif user==2 and pc ==1:
    print('Você VENCEU') 

elif user==3 and pc ==1:
    print('Você PERDEU')
elif user==3 and pc ==2:
    print('Você VENCEU')
else:   
    print('JOGADA INVALIDA')
    

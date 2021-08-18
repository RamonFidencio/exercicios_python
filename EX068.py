import random
cont=0
while True:
    pc = random.randint(1,10)
    con=0
    usu=int(input('Digite um valor: '))
    pi = input('PAR ou IMPAR [P/I]: ').upper()
    prd= (usu*pc)
    cont +=1
    if pi == 'P':
        if prd%2 ==0:
            print('\n\n','-'*30,'\nVOCE VENCEU !!!')
            print(f'Voce jogou {usu} e o computador {pc}. Total {prd} PAR')
        else:
            print('\n\n','-'*30,'\nVOCE PERDEU. GAME OVER {} tentativas'.format(cont))
            print(f'Voce jogou {usu} e o computador {pc}. Total {prd} IMPAR')
            break
    elif pi == 'I':
        if prd%2 ==0:
            print('\n\n','-'*30,'\nVOCE PERDEU. GAME OVER {} tentativas'.format(cont))
            print(f'Voce jogou {usu} e o computador {pc}. Total {prd} PAR')
            break
        else:
            print('\n\n','-'*30,'\nVOCE VENCEU !!!')
            print(f'Voce jogou {usu} e o computador {pc}. Total {prd} IMPAR')

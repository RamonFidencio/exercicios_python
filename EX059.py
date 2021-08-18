n1 = int (input ("Escolha um numero: "))
n2 = int (input ("Escolha um numero: "))
op=0
while op != 5:
    print('_'*40)
    print('NUMEROS ESCOLHIDOS: {} e {}'.format(n1,n2))
    print('\n\n[1] SOMA\n[2] MULTIPLICA\n[3] MAIOR\n[4] ESCOLHER NOVOS NUMEROS\n[5] SAIR')
    op = int(input('\nESCOLHA UMA DAS OPÇÔES: '))
    if op == 1:
        print('A SOMA DOS NUMEROS É: {}'.format(n1+n2))
        print('\n'*10)
    elif op == 2:
        print('O PRODUTO DOS NUMEROS É: {}'.format(n1*n2))
        print('\n'*10)
    elif op == 3:
        if n1>n2:
            print('O MAIOR É: {}'.format(n1))
            print('\n'*10)
        else:
            print('O MAIOR É: {}'.format(n2))
            print('\n'*10)
    elif op == 4:
        n1 = int (input ("Escolha o primeiro numero: "))
        n2 = int (input ("Escolha o segundo numero: "))
    elif op == 5:
        print("SAIU")
    else:
        print('OPÇÃO INVÁLIDA')
        

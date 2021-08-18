obra = {'char':0,'descricao':1,'ano':2}
painel1=[]
painel2=[]
painel3=[]
painel4=[]

def menu():
    op=int(input('\n[1] - Cadastrar obra\n[2] - Visualização dos Painéis\n[3] - Busca pelo identificador\n[4] - Estatísticas \n[5] - Lista de Obras\n\n[0] - Sair \n\n Digite a opção desejada:'))
    return op

def cadastra_obra(numero_painel):
    print(f'Cadastro de Obras no painel{numero_painel}\n\n')
    obra['char']=input('\n\nCaracter identificador: ')
    obra['descricao']=input('Descrição da obra: ')
    obra['ano']=(input('Ano : ')).upper()
    if obra['ano'] != int:
         obra['ano']=-1
    else:
        obra['ano']=int(obra['ano'])
    return obra

def op1():
    print(f'Cadastro de Obras\n\n')
    painel_cadastrar=int(input('Qual painel deseja cadastrar as obras: '))
    n_obras_cadastrar=int(input(f'Numero de obras a ser cadastrado no Painel {painel_cadastrar}: '))
    for i in range (0,n_obras_cadastrar):
        if painel_cadastrar == 1:
            painel1.append(cadastra_obra(painel_cadastrar))
        if painel_cadastrar == 2:
            painel2.append(cadastra_obra(painel_cadastrar))
        if painel_cadastrar == 3:
            painel3.append(cadastra_obra(painel_cadastrar))
        if painel_cadastrar == 4:
            painel4.append(cadastra_obra(painel_cadastrar))
    if painel_cadastrar == 1:
        for i,v in enumerate(painel1):
            print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    if painel_cadastrar == 1:
        for i,v in enumerate(painel2):
            print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    if painel_cadastrar == 1:
        for i,v in enumerate(painel3):
            print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    if painel_cadastrar == 1:
        for i,v in enumerate(painel4):
            print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
def op2(numero_busca=0):
    if numero_busca == 0:
        print(' Visualização dos Painéis\n\n')
        if len(painel1) > 0:
            for i,v in enumerate(painel1):
                print(f'{v["char"]} ',end='')
        print('\n')
        if len(painel2) > 0:
            for i,v in enumerate(painel2):
                print(f'{v["char"]} ',end='')
        print('\n')
        if len(painel3) > 0:
            for i,v in enumerate(painel3):
                print(f'{v["char"]} ',end='')
        print('\n')
        if len(painel4) > 0:
            for i,v in enumerate(painel4):
                print(f'{v["char"]} ',end='')
    else:
        if numero_busca == 1:
            for i,v in enumerate(painel1):
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
        if numero_busca == 2:
            for i,v in enumerate(painel1):
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
        if numero_busca == 3:
            for i,v in enumerate(painel1):
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
        if numero_busca == 4:
            for i,v in enumerate(painel1):
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
def op3():
    print(' Busca pelo identificador\n\n')
    ident=input('Qual o identificador: ')
    painel_busca=int(input('Em Qual painél deseja buscar: '))
    if ident ==1:
        op2(painel_busca)
        for i,v in enumerate(painel1):
            if(v["char"]) == painel_busca:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')       
    if ident ==2:
        op2(painel_busca)
        for i,v in enumerate(painel2):
            if(v["char"]) == painel_busca:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')  
    if ident ==1:
        for i,v in enumerate(painel3):
            if(v["char"]) == painel_busca:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    if ident ==1:
        for i,v in enumerate(painel4):
            if(v["char"]) == painel_busca:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
def op5():
    primeiro_ano=int(input('Ano: '))
    segundo_ano=int(input('Ano: '))
    print(f'Busca do ano {primeiro_ano} a {segundo_ano}:\n\n')
    for i,v in enumerate(painel1):
            if(v["ano"]) >= primeiro_ano and (v["ano"]) <= segundo_ano:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    for i,v in enumerate(painel2):
            if(v["ano"]) >= primeiro_ano and (v["ano"]) <= segundo_ano:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    for i,v in enumerate(painel3):
            if(v["ano"]) >= primeiro_ano and (v["ano"]) <= segundo_ano:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')
    for i,v in enumerate(painel4):
            if(v["ano"]) >= primeiro_ano and (v["ano"]) <= segundo_ano:
                print(f'\n{v["char"]} {v["descricao"]} {v["ano"]}')

while True:
    op=menu()
    if op ==1:
        op1()
    if op==2:
        op2()
    if op ==3:
        op3()
    if op ==5:
        op5()
    if op == 0:
        print('FIM !!!')
        break
    else:
        print('Opção Inválida')
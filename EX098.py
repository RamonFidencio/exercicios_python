def contador(inicio,fim,passa):
    for i in range (1,11,1):
        print(f'{i} ',end='')
    print('\n\n')
    for i in range (10,-2,-2):
        print(f'{i} ',end='')
    print('\n\n')
    if inicio>fim:
        fim=fim-passa
        passa=-passa
    for i in range (inicio,fim,passa):
        print(f'{i} - ',end='')
contador(1,100,10)
def leiaInt(texto):
    while True:
        txt=input(f'{texto}: ')
        if txt.isnumeric():
            return int(txt)
            break
        else:
            print('ERRO!  Digite um numero válido')

n = leiaInt('Digite um numero: ')
print(f'O numero que você digitou é: {n}')
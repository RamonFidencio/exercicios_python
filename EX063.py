n = int(input('QUANTOS NUMEOR QUER DA FIBONACCI? : '))
anterior =1
proximo=1
c=n/2
while c > 0:
    print('{} -> {} -> '.format(anterior,proximo),end='')
    anterior = anterior + proximo
    proximo = anterior + proximo
    c -=1
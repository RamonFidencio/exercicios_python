t = int(input('Numero: '))
r = int(input('Razão: '))
op=10
termo = t
cont =1
total =0
while op!=0:
    total = total+op
    while cont <= total:
        print(termo)
        termo += r
        cont +=1
    print("PAUSA")
    op = int(input('Mais quantos termos? '))
print('FIM')
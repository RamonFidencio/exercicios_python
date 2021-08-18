n = int(input("Digite um número inteiro não-negativo: "))
c = n
total = 1
while c > 0:
    total = total*c
    c=c-1
print('!{} = {}'.format(n,total))
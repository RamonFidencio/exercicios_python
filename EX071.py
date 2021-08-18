valor=int(input('QUANTO QUER SACAR: '))
cinquenta=0
vinte=0
dez=0
um=0
while True:
    while valor>=50:
        cinquenta+=1
        valor -=50
    while valor>=20:
        vinte+=1
        valor -=20
    while valor>=10:
        dez+=1
        valor -=10
    while valor >= 1:
        um+=1
        valor -=1
    break
print(f' \n{cinquenta}  NOTAS DE 50R$\n{vinte} NOTAS DE 20R$\n{dez} NOTAS DE 10R$\n{um} NOTAS DE 1R$')
temp=[]
pares=[]
impares=[]
for c in range (0,7):
    temp.append(int(input('Numero: ')))
    if temp[0]%2==0:
        pares.append(temp[0])
    else:
        impares.append(temp[0])
    temp.clear()

pares.sort()
impares.sort()

print(pares,'\n',impares)
import random
jogos=[]
temp=[]
c=0
n=int(input("Quantos jogos quer gerar? "))
for n in range (0,n):
    while len(temp) != 6:
        num=random.randint(0,60)
        if num not in temp:
            temp.append(num)
            c+=1
        else:
            c-=1
    jogos.append(temp[:])
    temp.clear() 
print(jogos)
        

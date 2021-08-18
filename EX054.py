from datetime import date
data = date.today().year
print(data)
cont1 =0
cont2 =0    
for pessoa in range (1,8):
    ano = int(input('Ano de nascimento: '))
    idade = data - ano
    if idade >= 18:
        cont1=cont1+1
    else:
        cont2=cont2+1

print("{} Pessoas são maiores\n{} Pessoas são menos ".format(cont1,cont2))
from datetime import datetime
data = datetime.now()
ano = int (input ("Ano de nascimento: "))
if (ano+18) > data.year:
    print('Faltam {} anos para se alistar'.format((18+(ano-data.year))))
elif (ano+18) == data.year:
    print('É hora de se alistar')
elif(ano+18) < data.year:
    print('Passaram {} anos do seu alistamento'.format(-(18+(ano-data.year))))
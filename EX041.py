from datetime import datetime
data = datetime.now()
nascimento = int (input ("Ano de nascimento: "))
ano = data.year - nascimento
if ano < 9:
    print('MIRIN')
elif ano < 14:
    print('INFANTIL')
elif ano < 19:
    print('JUNIOR')
elif ano < 20:
    print('SENIOR')
else:
    print('MASTER')
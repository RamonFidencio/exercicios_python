from datetime import datetime
dados={}
dados['nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
dados['idade']=datetime.now().year-nasc
dados['ctps'] = int(input('Carteira de Trabalho: '))
if dados['ctps'] != 0:
    dados['contratacao']=int(input('Ano de Contratação: '))
    dados['Salario']=float(input('Salário: '))
    dados['aposentadoria']= dados['idade'] + ((dados['contratacao']+35)-datetime.now().year)
print('-='*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')
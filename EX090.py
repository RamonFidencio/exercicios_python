alu={'nome':'','media':0,'situacao':''}
alu['nome']=input('Nome: ')
alu['media']=int(input(f'Media de {alu["nome"]: }'))
if alu['media'] >= 7:
    alu['situacao']='APROVADO'
else:
    alu['situacao']='REPROVADO'
print(f'O {alu["nome"]} está: {alu["situacao"]}')
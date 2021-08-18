def notas(*notas):
    relatorio=dict()
    relatorio['Tamanho']=len(notas)
    soma=0
    for i in notas:
        if i == notas[0]:
            men=notas[0]
            mai=notas[0]
        if len(notas)==1 :
            mai=notas
            men=notas[0]
        else:
            if i > mai:
                mai=i
            if i<men:
                men=i
        soma+=i
    relatorio['maior']=mai
    relatorio['menor']=men
    relatorio['media']=soma/len(notas)
    if relatorio['media']>=7:
        relatorio['situação']="APROVADO"
    else:
        relatorio['situação']="REPROVADO"

    return print(relatorio)

notas(5,8,1,6,7,9,15,10)
from datetime import datetime
def voto(ano):
    idade=datetime.now().year-ano
    if idade<16:
        print('NEGADO')
    elif idade>=16 and idade<18:
        print('OPCIONAL')
    else:
        print('OBRIGATÓRIO')
    


voto(2010)

km = float(input ("Distancia: "))
if(km>200):
    print("Sua viagem vai custar R$ {}".format(km*0.45))
else:
    print("Sua viagem vai custar R$ {}".format(km*0.5))

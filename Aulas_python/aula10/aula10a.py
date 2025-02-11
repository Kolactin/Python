# condicional

tempo = int(input("Quantos anos tem seu carro?"))

if (tempo == 1):
    print("Seu carro é novo, pois tem apenas {} ano".format(tempo))
elif (tempo <= 10):
    print("Seu carro é novo, pois tem apenas {} anos".format(tempo))
else:
    print("Seu carro é velho, pois já tem {} anos".format(tempo))

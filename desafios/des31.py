distVia = int(input("Qual a distância da viagem (em Km)?"))

if distVia <= 200:
   preco = distVia * 0.5
else:
    preco = distVia * 0.45

print("O valor da viagem é R${}".format(preco))

vel = float(input("Qual a velocidade do carro?"))
lim = 70
multa = (vel - lim) * 7

if (vel > lim):
    print("Você foi multado em R${}".format(multa))
else:
    print("Você está dentro do limite de velocidade permitido")

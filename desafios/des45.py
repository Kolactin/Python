import random
opcoes = ["pedra", "papel", "tesoura"]
rob = random.choice(opcoes)
huma = input("informe sua opção: (pedra / papel / tesoura)")

hum = huma.lower()

if hum == "pedra" or hum == "papel" or hum == "tesoura":
    if hum != rob:
        if hum == "pedra":
                if  rob == "tesoura":
                    print("VOCÊ VENCEU!")
                else:
                    print("PERDEU")
        if hum == "tesoura":
                if  rob == "papel":
                    print("VOCÊ VENCEU!")
                else:
                    print("PERDEU")
        if hum == "papel":
                if  rob == "pedra":
                    print("VOCÊ VENCEU!")
                else:
                    print("PERDEU")
    else:
        print("EMPATE")
else:
    print("informe uma opção válida!")

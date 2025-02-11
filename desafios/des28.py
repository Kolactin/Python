import random
from time import sleep
end = 10

esc = random.randint(1,end) # Gera um número aleatório
usu = int(input("Escolha um valor entre 0 e {}:".format(end)))

if (usu > 10 ):
    print("Você escolheu um valor inválido!")
else:
    print("PROCESSANDO...")
    sleep(2)
    if (esc == usu):
        print("Parabéns, você venceu!")
    else:
        print("Que pena, você perdeu! O número era {}".format(esc))

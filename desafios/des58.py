import random
from time import sleep
end = 10
esc = random.randint(1,end) # Gera um número aleatório
usu = ""
qntd = 0

while usu != esc:
    qntd += 1
    usu = int(input("Escolha um valor entre 0 e {}:".format(end)))

    if usu > end :
        print("Você escolheu um valor inválido!")
    else:
        print("PROCESSANDO...")
        sleep(2)
        if (esc == usu):
            print("Parabéns, você venceu!")
        else:
            print("Tente novamente!")

print("Voce precisou de {} tentativas para acertar!".format(qntd))
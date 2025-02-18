n1 = int(input("Insira o primeiro valor"))
n2 = int(input("Insira o segundo valor"))
r = 0
maior = 0

while r < 5:
    print()
    print("Qual operação você deseja executar?")
    r = int(input("1 - SOMAR || 2 - MULTIPLICAR || 3 - MAIOR || 4 NOVOS NÚMEROS || 5 FINALIZAR"))
    if r == 1:
        resp = n1 + n2
        print("A soma entre {} e {} resulta em {}".format(n1, n2, resp))
    elif r == 2:
        resp = n1 * n2
        print("A multiplicação entre {} e {} resulta em {}".format(n1, n2, resp))
    elif r == 3:
        if n1 > n2:
            maior = n1
            print("O maior número é {}".format(maior))
        elif n2 > n1:
            maior = n2
            print("O maior número é {}".format(maior))
        elif n1 == n2:
            print("Não há número maior, ambos possuem o mesmo valor")
    elif r == 4:
        n1 = int(input("Insira o primeiro valor"))
        n2 = int(input("Insira o segundo valor"))
    else:
        print("Fim do programa!")

if r > 5:
    print("Insira uma opção válida")
    r = 0

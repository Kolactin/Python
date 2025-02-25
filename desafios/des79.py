n = []
r = 0
c= 1

while r != 2:

    num = int(input(f"informe o {c}º valor:"))

    if num in n:
        print("Esse número já foi implementado na lista!")
    else:
        n.append(num)
        print("Número adicionado à lista")

    print("deseja adicionar outros valores?")
    r = int(input("1 - SIM || 2 - NÃO"))

    while r not in (1, 2):
        print("Por favor, escolha uma das seguintes opções!")
        r = int(input("1 - SIM || 2 - NÃO: "))

    c += 1

n.sort()
print(f"A lista, em ordem crescente, é {n}")

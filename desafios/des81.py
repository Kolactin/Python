lis = []
c = 1
r = 0

while r != 2:
    n = int(input(f"Informe o {c} valor:"))
    lis.append(n)
    print(f"O número {n} foi adicionado à lista")

    print("Deseja adicionar outro número?")
    r = int(input("1 - SIM || 2 - NÃO"))
    while r not in(1, 2):
        print("Informe uma opção válida!")
        print("Deseja adicionar outro número?")
        r = int(input("1 - SIM || 2 - NÃO"))

    c += 1

lis.sort(reverse=True)
print("-_"*20)
print(f"A lista, em ordem decrescente, fica: {lis}")
print("-_"*20)
print(f"Você digitou {(c-1)} números")

print("-_"*20)
if 5 in lis:
    print("O número 5 está presente na lista!")
else:
    print("O número 5 não está incluso na lista!")
print("-_"*20)
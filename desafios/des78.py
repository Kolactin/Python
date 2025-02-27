lista = []
comp = int(input("Informe o valor inicial da lista"))
c = 0
maior = menor = 0
while c < comp:
    num = int(input("Informe um valor"))
    lista.append(num)

    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]

    c += 1

print(f"O maior valor foi {maior} nas posições:", end="")
for pos, n in enumerate(lista):
    if n == maior:
        print(f" {pos}...", end="")

print("")

print(f"O menor valor está na posições:", end="")
for pos, n in enumerate(lista):
    if n == menor:
            print(f" {pos}...", end="")

print("")
print("-_"*20)
print(f"Você digitou {len(lista)} números! A lista é composta por {lista}")

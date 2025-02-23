lista = []
comp = int(input("Informe o tamanho inicial da lista"))
c = 0

while c < comp:
    num = int(input("Informe o valor a ser adicionado à lista"))
    lista.append(num)
    c += 1

print(f"A lista é composta por {lista}")

print(f"De forma crescente, temos: {sorted(lista)}")

print(f"De forma decrescente, temos: {sorted(lista, reverse=True)}")

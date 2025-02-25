lista = []
comp = int(input("Informe o valor inicial da lista"))
c = 0

while c < comp:
    num = int(input("Informe um valor"))
    lista.append(num)
    c += 1

maior = menor = lista[0]
pMaior = pMenor = []

for pos, n in enumerate(lista):
    if n >= maior:
        iMa = 0
        maior = n
        pMaior.append(pos)
        iMa += 1


    if n <= menor:
            iMe = 0
            menor = n
            pMenor.append(pos)
            iMe += 1

print(f"A lista é composta por {lista}, sendo o maior número {maior} na posição {pMaior} e o menor número {menor} na posição {pMenor}")

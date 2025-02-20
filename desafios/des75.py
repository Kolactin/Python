n = (int(input("Digite o primeiro valor")), int(input("Digite o segundo valor")), int(input("Digite o terceiro valor")), int(input("Digite o quarto valor")))
c9 = 0
nP = 0
for pos, c in enumerate(n):
    if n[pos] == 9:
        c9 += 1

    if n[pos] % 2 == 0:
        print(f"{c} é um número par!")


n3 = n.index(3)

print(f"O número 9 aparece {c9} vezes")
print(f"O número 3 aparece, na primeira vez na posição {n3}")
'TEMA DA AULA: TUPLA (variável composta)'

n = (10,53,95,12) # Tuplas são imutáveis
lanche = ("ham", "suco", "pizza", "Pudim")

# print(len(n))
print(sorted(lanche))
print(sorted(n))
for pos, cont in enumerate(n):
    print(f"O número {cont} está na posição {pos}")

for c in lanche:
    print(f"Eu vou comer {c}")

# f"texto" = (print formatado!)

a = (7, 1, 9)
b = (1, 9, 1, 8)
c = a + b
n = 9

print(f"O número {n}, aparece {c.count(n)} vezes") # mostra quantas vezes aparece o número n
print(f'Organizado, a tupla c, fica:')
print(f"{sorted(c)}")

from random import randint

n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

maior = menor = n[1]

for c in range(0, 5):
    if n[c] > maior:
        maior = n[c]
    elif n[c] < menor:
        menor = n[c]

print("Os números escolhidos foram:")
print(n)

print("^^"*20)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
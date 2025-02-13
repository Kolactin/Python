maior = 0
menor = 300

for c in range(0,5):
    p = int(input("Informe seu peso (em Kg)"))
    if p > maior:
        maior = p
    elif p < menor:
        menor = p
print("O maior peso medido foi {} e o menor peso medido foi {}".format(maior, menor))

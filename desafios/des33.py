n1 = float(input("Informe o primeiro valor:"))
n2 = float(input("Informe o segundo valor:"))
n3 = float(input("Informe o terceiro valor:"))

maior = 0
menor: float

if n1 > n2:
    maior = n1
elif n3 > n2:
    maior = n3
else:
    maior = n2

if n1 < n2:
    menor = n1
elif n3 < n2:
    menor = n3
else:
    menor = n2

print("O maior valor é {} e o menor valor é {}".format(maior, menor))
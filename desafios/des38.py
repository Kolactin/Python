n1 = float(input("Selecione um número:"))
n2 = float(input("Selecione outro número:"))

if n1 > n2:
    print("O primeiro valor é maior")
elif n2 > n1:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, ambos os valores são iguais")
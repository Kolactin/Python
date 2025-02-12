n1 = float(input("informe a primeira nota do aluno:"))
n2 = float(input("informe a segunda nota do aluno:"))

med = (n1 + n2) / 2
print("A média do estudante é {}".format(med))
if med < 5:
    print("REPROVADO!")
elif 5 <= med < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
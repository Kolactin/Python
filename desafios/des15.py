dias = int(input("Quantos dias alugados?"))
km = float(input("Quantos kms rodados?"))
pay = (dias * 60.75) + (km * 0.157)
print("O total a se pagar é de R${:.2f}".format(pay))

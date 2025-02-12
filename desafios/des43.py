p = float(input("informe seu peso:"))
ac = float(input("informe sua altura: (EX: 180)"))

a = ac / 100
imc = p / (a**2)
print("Seu IMC é: {}".format(imc))
if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc <= 25:
    print("PESO IDEAL")
elif imc < 30:
    print("SOBREPESO")
elif imc <= 40 :
    print("OBESIDADE")
else:
    print("OBESIDADE MÓRBIDA")

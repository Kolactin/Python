sal = float(input("Informe seu salário:"))




if sal > 1250:
    aum = int(10/100)
    newSal = sal * aum
else:
    aum = int(15/100)
    newSal = sal * aum

tot = sal + newSal
print("Seu aumento salarial é de {}% resultando em um aumento de R${}. O que, por sua vez, resulta em: R${} de salário".format((aum*100),newSal, tot))

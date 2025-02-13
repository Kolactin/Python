totId = 0
old = 0
adoWoman = 0

for c in range(0,4):
    nome = input("Informe o nome da {}ª pessoa:".format(c+1))
    idade = int(input("Informe a idade de {}:".format(nome)))
    sexo = int(input("Informe o sexo de {}: 1 - FEMININO || 2 - MASCULINO".format(nome)))

    totId += idade

    if idade > old and sexo == 2:
        oldName = nome
        old = idade
        homem = "O homem mais velho é {}".format(oldName)

    if idade < 20 and sexo == 1:
        adoWoman += 1
        mulher = "Existem {} mulheres abaixo de 20 anos".format(adoWoman)

med = totId / 4

print("A média da idade go grupo é {}".format(med))
print(homem)
print(mulher)

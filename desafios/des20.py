import random
n1 = input("Insira o nome do primeiro aluno")
n2 = input("Insira o nome do segundo aluno")
n3 = input("Insira o nome do terceiro aluno")
n4 = input("Insira o nome do quarto aluno")
esc = random.choice((n1,n2,n3,n4))
# sor = random.choices(esc, k=4) repete
ap = random.sample((n1,n2,n3,n4), k=4) # não repete
print("A ordem de apresentação é: {}".format(ap))

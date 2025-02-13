p = 0
for c in range(1,7):
    age = int(input("Informe a idade do {}º paciente ".format(c)))
    if age < 18 :
        p += 1
print("{} pacientes não atingiram a maioridade".format(p))

age = int(input("Informe sua idade"))

if age < 18:
    tempo = 18 - age
    print("Ainda restam {} ano(s) para realizar seu alistamento".format(tempo))
elif age > 18:
    tempo = age - 18
    print("Há {} ano(s) atrás era para você realizar seu alistamento".format(tempo))
elif age == 18:
    print("Você está na idade correta de se alistar")


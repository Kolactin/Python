pT = int(input("Informe o primeiro termo da PA:"))
ra = int(input("Informe a razão da PA:"))
uT = 0
ter = 10
c = 1
r = ""

while r != 'n':
    while c <= ter:
        uT = pT + (ra * (c-1))
        print(uT)
        c += 1

    respo = str(input("deseja verificar mais termos?[S/N]"))
    r = respo.lower()
    if r == "s":
        acre = int(input("Quantos termos a mais?"))
        ter += acre
    elif r == "n":
        print("Obrigado pela visita!")

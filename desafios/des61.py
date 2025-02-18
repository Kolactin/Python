pT = int(input("Informe o primeiro termo da PA:"))
ra = int(input("Informe a razão da PA:"))
uT = 0
c = 1

while c <= 10:
    uT = pT + (ra * (c-1))
    print(uT)
    c += 1
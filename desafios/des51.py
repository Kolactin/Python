pT = int(input("Informe o primeiro termo da PA:"))
ra = int(input("Informe a razão da PA:"))
uT = 0

for c in range(1, 11, 1):
    uT = pT + (ra * (c-1))
    print(uT)
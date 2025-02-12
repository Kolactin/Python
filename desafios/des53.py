pal = input("Informe uma frase /palavra para saber se é um palíndromo")
pala = pal.upper()
palaNS = pala.split()
palaI = pala[::-1]
palaiNS = palaI.split()
print("A palavra {} resulta em {}".format(pala,palaiNS))

if palaiNS == palaNS:
    print("É PALÍNDROMO")
else:
    print("NÃO É PALÍNDROMO!")

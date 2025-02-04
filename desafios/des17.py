from math import sqrt
co = float(input("Insira o valor do cateto oposto"))
ca = float(input("Insira o valor do cateto adjacente"))
hipo = sqrt((co ** 2) + (ca ** 2))
print("O valor da hipotenusa é {:.2f}".format(hipo))

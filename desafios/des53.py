pal = str(input("Informe uma frase /palavra para saber se é um palíndromo")).strip().upper() # tira espaços antes e dps e deixa maiúscula
palS = pal.split()
palavra = "".join(palS)
inverso = ""

for c in range(len(palavra)-1, -1,-1):
    inverso += palavra[c]

if palavra == inverso:
    print("É UM PALÍNDROMO!")
else:
    print("NÃO É PALÍNDROMO!")

print("O inverso de {}, é {}".format(palavra, inverso))

# o for pode ser substituido pela solução utilizando o metodo [::-1]

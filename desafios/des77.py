palavras = ("sol", "montanha", "guitarra", "oceano", "felicidade")
vog = ("a", "e", "i", "o", "u")

for p in palavras:
    print(f"\n Na palavra {p.upper()}, temos ", end ="")
    for letra in p:
        if letra.lower() in vog:
            print(letra,"", end="")
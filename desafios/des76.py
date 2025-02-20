itens = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00)
print("=^=" * 20)
pos = 0

while pos < len(itens) - 1:
    print(f"{itens[pos]}", ("." * 20), "R${:.2f}".format(itens[pos+1]))
    pos += 2

print("=^=" * 20)
s = 0
n = 0
for c in range(1, 7, 1):
    n = int(input("Informe um valor"))
    if n % 2 == 0:
        s += n
print("A soma entre os números digitados que são pares, resulta em: {}".format(s))

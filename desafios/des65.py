n = int(input("Informe um valor"))
r = ""
c = 0
med = 0
maior = n
menor = n

while r != "n":
    n = int(input("Informe um valor"))
    print("Deseja continuar?")
    resp = str(input("[S/N]?"))
    r = resp.lower()

    if n > maior:
        maior = n

    if n < menor:
        menor = n
    med = med + n
    c += 1

medF = med / c

print("Você digitou {} números". format(c))
print("A media entre eles é de {}".format(medF))
print("O maior e menor valor, respectivaente, é {} e {}".format(maior, menor))

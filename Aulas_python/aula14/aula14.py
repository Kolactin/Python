'''for c in range(0,10):
    print(c)
print("FIM!")

c = 1
while c <= 10:
    print(c)
    c += 1
print("FIM")'''

r = "s"
par = impar = 0
n = 1
while n != 0:
    n = int(input("Informe um valor"))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números ímpares!".format(par, impar))

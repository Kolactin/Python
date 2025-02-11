num = int(input("Informe um número"))

if (num % 2 == 0):
    print("O número {} é Par".format(num))
else:
    print("O número {} é ímpar".format(num))

if (num < 0):
    print("Seu módulo, pois {} é negativo!".format(num))
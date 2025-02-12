a = int(input("Informe um valor para a primeira reta:"))
b = int(input("Informe um valor para a Segunda reta:"))
c = int(input("Informe um valor para a terceira reta:"))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("É possível formar um triângulo com esses valores!")
    if a == b and b == c:
        print("EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("ISÓSCELES")
    else:
        print("LADOS DIFERENTES")
else:
    print("É impossível formar um triângulo com esses valores!")

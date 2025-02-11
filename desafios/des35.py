a = int(input("Informe um valor para a primeira reta:"))
b = int(input("Informe um valor para a Segunda reta:"))
c = int(input("Informe um valor para a terceira reta:"))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("É possível formar um triângulo com esses valores!")
else:
    print("É impossível formar um triângulo com esses valores!")

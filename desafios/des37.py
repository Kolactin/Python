num = int(input("informe um número para a conversão:"))
print("informe a opção de conversão")
esc = int(input("1 - Binário || 2 - octal || 3 - hexadecimal || 4 - todas as opções"))

# binário
if esc == 1:
    bina = bin(num)
    pBina = "O número {} em binário é: {}".format(num,bina)
    print(pBina)
if esc == 2:
    octal = oct(num)
    pOctal = "O número {} em octal é {}".format(num,octal)
    print(pOctal)
if esc == 3:
    hexa = hex(num)
    pHexa = "O número {} em hexadecimal é {}".format(num,hexa)
    print(pHexa)
if esc >= 4:
    print("informe uma opção válida!")
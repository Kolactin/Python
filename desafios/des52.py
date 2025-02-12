num = int(input("Informe um número para saber se ele é primo:"))

if num % 1 == 0 and num % 2 != 0 and num % 3 != 0 and num % num == 0:
    print("É primo!")
else:
    print("Não é primo!")

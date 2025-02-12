ano = int(input("Informe seu ano de nascimento"))

age = 2025 - ano

if age <= 9:
    print("MIRIM")
elif age <= 14:
    print("INFANTIL")
elif age <= 19:
    print("JUNIOR")
elif age <= 20:
    print("SENIOR")
else:
    print("MASTER")

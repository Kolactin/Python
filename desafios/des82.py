nums = []
imp = []
par = []
num = c = 1

while num != 0:
    print("Digite 0 para encerrar o programa!")
    num = int(input(f"Informe o {c} valor:"))
    nums.append(num)

    if num %2 == 0:
        par.append(num)
    else:
        imp.append(num)

    c += 1

print(f"Os valores digitados foram: {nums}")
print("-"*20)
print(f"Os valores ímpares são: {imp}")
print("-"*20)
print(f"Os valores pares são: {par}")
print("-"*20)
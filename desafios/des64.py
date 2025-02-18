num = 0
res = 0
count = -1
cMe = 0
cMa = 0

while num != 999:
    if num != 999:
        num = int(input("Informe um número"))
        res = res + num
        count += 1

    if num < 999:
        cMe += 1
    elif num > 999:
        cMa += 1

if count != 0:
    print("Você digitou {} números, sendo {} menores que 999 e {} maiores que 999 e a soma entre eles é de: {}".format(count ,cMe ,cMa ,res))
else:
    print("Você encerrou o programa sem informar valores!")